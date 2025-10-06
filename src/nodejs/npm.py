#!/usr/bin/env python3


"""Expose npm’s binary."""


from .command_that_might_be_a_script import CommandThatMightBeAScript
from .node_path import NODE_PATH


class Npm(CommandThatMightBeAScript):
    """Expose npm’s binary."""

    _command_name = "npm"
    _script_name = (
        NODE_PATH
        / "lib"
        / "node_modules"
        / f"{_command_name}"
        / "bin"
        / f"{_command_name}-cli.js"
    )
