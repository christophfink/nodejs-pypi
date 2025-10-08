#!/usr/bin/env python3


"""Expose npx’s binary."""


__all__ = ["npx"]


import sys

from .maybe_script import MaybeScript
from .node_path import NODE_PATH


class Npx(MaybeScript):
    """Expose npx’s binary."""

    _command_name = "npx"
    _script_name = NODE_PATH / "lib" / "node_modules" / "npm" / "bin" / "npx-cli.js"


npx = Npx()


if __name__ == "__main__":
    sys.exit(npx.main(*sys.argv[1:]))
