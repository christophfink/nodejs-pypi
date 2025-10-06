#!/usr/bin/env python3


"""Expose npx’s binary."""


__all__ = ["npx"]


import sys

from .command_that_might_be_a_script import CommandThatMightBeAScript
from .node_path import NODE_PATH


class Npx(CommandThatMightBeAScript):
    """Expose npx’s binary."""

    _command_name = "npx"
    _script_name = (
        NODE_PATH / "lib" / "node_modules" / "npm" / "bin" / f"{_command_name}-cli.js"
    )


npx = Npx()


if __name__ == "__main__":
    sys.exit(npx.main(*sys.argv[1:]))
