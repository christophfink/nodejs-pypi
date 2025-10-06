#!/usr/bin/env python3


"""Utilities to download the correct node version."""


__all__ = ["NodeJsDownloader"]


import functools
import pathlib
import shutil
import sys
import tempfile
import zipfile

if sys.version_info > (3, 11):
    import tarfile
else:
    from backports import tarfile

from remote_path import RemotePath

PACKAGE = "nodejs.build_backend"

NODEJS_DOWNLOAD_URL = (
    "https://nodejs.org/dist/v{node_version}/"
    "node-v{node_version}-{node_platform}.{file_extension}"
)
UNOFFICIAL_BUILDS_NODEJS_DOWNLOAD_URL = (
    "https://unofficial-builds.nodejs.org/download/release/v{node_version}/"
    "node-v{node_version}-{node_platform}.{file_extension}"
)

INIT_PY = next(pathlib.Path().glob("src/*/__init__.py"))


class NodeJsDownloader:
    """Context manager for an ephemeral copy of node.js."""

    def __init__(self, platform, destination_directory):
        """Context manager for an ephemeral copy of node.js."""
        self.platform = platform
        self.destination_directory = pathlib.Path(destination_directory)

    def __enter__(self):
        """Enter context."""
        archive = self.archive(self.platform)
        if archive.suffix == ".zip":
            with tempfile.TemporaryDirectory() as temporary_directory:
                with zipfile.ZipFile(archive) as z:
                    z.extractall(temporary_directory)
                shutil.move(
                    (pathlib.Path(temporary_directory) / archive.stem).resolve(),
                    self.destination_directory.resolve(),
                )
        elif archive.suffix == ".xz":
            self.destination_directory.mkdir(parents=True, exist_ok=True)

            def _filter(member, path):
                member = tarfile.tar_filter(member, path)
                if member is not None:
                    try:  # remove top directory component
                        member.name = member.name.split("/", maxsplit=1)[1]
                    except IndexError:  # top directory
                        member = None
                return member

            with tarfile.open(archive) as f:
                f.extractall(self.destination_directory, filter=_filter)

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit context."""
        # restore _node empty except .keep
        shutil.rmtree(self.destination_directory)
        self.destination_directory.mkdir()
        (self.destination_directory / ".keep").touch()

    def archive(self, platform):
        """Download node.js before building a wheel."""
        node_download_url = self.get_download_url(platform, self.version)
        archive = RemotePath(node_download_url)
        return archive

    @staticmethod
    def get_download_url(node_platform, node_version):
        """Determine the URL from which to download node.js."""
        if node_platform.startswith("win"):
            file_extension = "zip"
        else:
            file_extension = "tar.xz"
        if "musl" in node_platform:
            node_download_url = UNOFFICIAL_BUILDS_NODEJS_DOWNLOAD_URL.format(
                node_version=node_version,
                node_platform=node_platform,
                file_extension=file_extension,
            )
        else:
            node_download_url = NODEJS_DOWNLOAD_URL.format(
                node_version=node_version,
                node_platform=node_platform,
                file_extension=file_extension,
            )
            return node_download_url

    @functools.cached_property
    def version(self):
        """Find the version of the nodejs Python package we are building."""
        values = {"__name__": PACKAGE}
        exec(INIT_PY.read_text(), values)
        return values["__version__"][1:]
