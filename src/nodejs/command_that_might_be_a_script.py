#!/usr/bin/env python3


"""Base class for the commands that might be scripts (npm, npx, corepack)."""


import functools

from .base_command import BaseCommand
from .node import Node
from .node_path import NODE_PATH


class CommandThatMightBeAScript(BaseCommand):
    """Base class for the commands that might be scripts (npm, npx, corepack)."""

    _command_name = None

    @functools.cached_property
    def _script_name(self):
        return (
            NODE_PATH
            / "lib"
            / "node_modules"
            / f"{self._command_name}"
            / "bin"
            / f"{self._command_name}-cli.js"  # override for corepack ;)
        )

    @functools.cached_property
    def _command(self):
        assert self._command_name is not None
        try:
            command = NODE_PATH / "bin" / f"{self._command_name}"
            assert command.is_file() or command.is_symlink()
            return Node()._command + [self._script_name]
        except AssertionError:
            try:
                command = NODE_PATH / f"{self._command_name}.cmd"
                assert command.is_file()
                return [command]
            except AssertionError as exception:
                raise RuntimeError(
                    f"Could not find {self._command_name} executable."
                ) from exception
