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


def main():
    """Run command line."""
    sys.exit(npx.call(*sys.argv[1:]))


if __name__ == "__main__":
    main()
