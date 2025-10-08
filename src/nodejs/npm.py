#!/usr/bin/env python3


"""Expose npm’s binary."""


__all__ = ["npm"]


import sys

from .maybe_script import MaybeScript
from .node_path import NODE_PATH


class Npm(MaybeScript):
    """Expose npm’s binary."""

    _command_name = "npm"
    _script_name = NODE_PATH / "lib" / "node_modules" / "npm" / "bin" / "npm-cli.js"


npm = Npm()


if __name__ == "__main__":
    sys.exit(npm.main(*sys.argv[1:]))
