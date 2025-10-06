#!/usr/bin/env python3


"""Expose corepack’s binary."""


from .command_that_might_be_a_script import CommandThatMightBeAScript
from .node_path import NODE_PATH


class Corepack(CommandThatMightBeAScript):
    """Expose corepack’s binary."""

    _command_name = "corepack"
    _script_name = (
        NODE_PATH
        / "lib"
        / "node_modules"
        / f"{_command_name}"
        / "dist"
        / f"{_command_name}.js"  # override for corepack ;)
    )
