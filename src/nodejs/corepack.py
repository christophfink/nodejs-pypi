#!/usr/bin/env python3


"""Expose corepack’s binary."""


__all__ = ["corepack"]


import sys

from .command_that_might_be_a_script import CommandThatMightBeAScript
from .node_path import NODE_PATH


class Corepack(CommandThatMightBeAScript):
    """Expose corepack’s binary."""

    _command_name = "corepack"
    _script_name = (
        NODE_PATH / "lib" / "node_modules" / "corepack" / "dist" / "corepack.js"
    )


corepack = Corepack()


if __name__ == "__main__":
    sys.exit(corepack.main(*sys.argv[1:]))
