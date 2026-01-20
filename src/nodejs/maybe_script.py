#!/usr/bin/env python3


"""Base class for the commands that might be scripts (npm, npx)."""

import functools

from .base_command import BaseCommand
from .node import Node
from .node_path import NODE_PATH


class MaybeScript(BaseCommand):
    """Base class for the commands that might be scripts (npm, npx)."""

    _command_name = None
    _script_name = None

    @functools.cached_property
    def _command(self):
        try:
            assert self._command_name is not None
            assert self._script_name is not None
        except AssertionError:
            raise NotImplementedError(
                "Do not use MaybeScript directly. "
                "Rather, inherit from it and define the child class’ "
                "_command_name and _script_name attributes."
            )
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
