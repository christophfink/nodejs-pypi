#!/usr/bin/env python3


"""Expose node’s binary."""


import functools

from .base_command import BaseCommand
from .node_path import NODE_PATH


class Node(BaseCommand):
    """Expose node’s binary."""

    @functools.cached_property
    def _command(self):
        for command in [
            NODE_PATH / "bin" / "node",
            NODE_PATH / "node.exe",
        ]:
            try:
                assert command.exists()
                assert command.is_file()
                return [command]
            except AssertionError:
                continue
        raise RuntimeError("Could not find node executable.")
