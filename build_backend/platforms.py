#!/usr/bin/env python3


"""
Define platform compatibility tags and their relation to node versions.

These lookup tables are based on information from:
    https://github.com/nodejs/node/blob/main/BUILDING.md#platform-list
    https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/

"""


import os
import platform

__all__ = ["override_platform", "target_platforms"]

NODE_PLATFORM_BY_PYTHON_PLATFORM = {
    "win_amd64": "win-x64",
    "win32": "win-x86",
    "macosx_13_5_x86_64": "darwin-x64",
    "macosx_13_5_arm64": "darwin-arm64",
    "manylinux_2_28_x86_64": "linux-x64",
    "manylinux_2_28_aarch64": "linux-arm64",
    "musllinux_1_1_x86_64": "linux-x64-musl",
}
NODE_PLATFORMS = list(NODE_PLATFORM_BY_PYTHON_PLATFORM.values())

PYTHON_PLATFORM_BY_NODE_PLATFORM = {
    value: key for key, value in NODE_PLATFORM_BY_PYTHON_PLATFORM.items()
}
PYTHON_PLATFORMS = list(PYTHON_PLATFORM_BY_NODE_PLATFORM.values())


def local_platform():
    """Determine the best fit between available platforms."""
    platform_tag = None
    system = platform.system()
    if system == "Linux":
        architecture = os.uname().machine
        libc = platform.libc_ver()[0]
        if libc == "glibc":
            platform_tag = f"manylinux_2_28_{architecture}"
        else:  # alpine does not report platform.libc_ver()
            platform_tag = f"musllinux_1_1_{architecture}"
    elif system == "Darwin":
        architecture = os.uname().machine
        platform_tag = f"macosx_13_5_{architecture}"
    elif system == "Windows":
        architecture = platform.machine()
        if architecture == "ARM64":
            platform_tag = "win_arm64"
        elif architecture == "AMD64":
            platform_tag = "win_amd64"
        else:
            platform_tag = "win32"
    return platform_tag


def override_platform(config_settings):
    """Add a build option to produce a binary wheel."""
    _, python_platform = target_platforms(config_settings)

    config_settings = config_settings or {}
    if "--build_option" not in config_settings:
        config_settings["--build-option"] = []
    config_settings["--build-option"].append(f"--plat-name={python_platform}")

    return config_settings


def target_platforms(config_settings):
    """Determine node and python target platforms from config_settings."""
    try:
        target_platform = config_settings["target-platform"]
        if target_platform in PYTHON_PLATFORMS:
            python_platform = target_platform
            node_platform = NODE_PLATFORM_BY_PYTHON_PLATFORM[python_platform]
        elif target_platform in NODE_PLATFORMS:
            node_platform = target_platform
            python_platform = PYTHON_PLATFORM_BY_NODE_PLATFORM[node_platform]
        else:
            raise ValueError(
                (
                    f"Target platform '{target_platform}' not recognised. \n"
                    "Available platform identifiers are: "
                    + (", ".join(NODE_PLATFORMS + PYTHON_PLATFORMS))
                )
            )
    except (KeyError, TypeError):
        python_platform = local_platform()
        node_platform = NODE_PLATFORM_BY_PYTHON_PLATFORM[python_platform]

    return node_platform, python_platform
