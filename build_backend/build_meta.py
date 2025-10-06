#!/usr/bin/env python3


"""
A custom build backend that includes node.js.

This build backend downloads the node.js version equivalent to this package’s
version (i.e., if nodejs.__version__ is 22.20.0, node.js v22.20.0 will be
downloaded and re-packed). It also supports cross-packing for a different
platform. For instance, call

`python -m build --wheel --config-setting target-platform="win-x64"`

to build for 64-bit Windows. The config setting accepts both node.js and Python
platform identifiers.
"""

__all__ = [
    "build_sdist",
    "build_wheel",
    "get_requires_for_build_sdist",
    "get_requires_for_build_wheel",
    "prepare_metadata_for_build_wheel",
]


import pathlib

import setuptools.build_meta
from nodejs_downloader import NodeJsDownloader
from platforms import override_platform, target_platforms
from setuptools.build_meta import (
    build_sdist,
    get_requires_for_build_sdist,
    prepare_metadata_for_build_wheel,
)

BUILD_REQUIREMENTS = [
    "build",
    "pyproject_hooks",
    "requests",
    "xdg-base-dirs; python_version > '3.9'",
    "xdg; python_version < '3.10'",
]
NODEJS_DIRECTORY = pathlib.Path("src/nodejs/_node/")


def build_wheel(
    wheel_directory,
    config_settings=None,
    metadata_directory=None,
):
    """Override setuptools.build_meta."""
    config_settings = override_platform(config_settings)
    node_platform, _ = target_platforms(config_settings)

    with NodeJsDownloader(node_platform, NODEJS_DIRECTORY):
        wheel = setuptools.build_meta.build_wheel(
            wheel_directory, config_settings, metadata_directory
        )
    return wheel


def get_requires_for_build_wheel(config_settings=None):
    """Override setuptools.build_meta."""
    return BUILD_REQUIREMENTS
