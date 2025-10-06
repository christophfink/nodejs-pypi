#!/usr/bin/env python3


"""Wraps the Node.js JavaScript runtime environment."""


import sys

from . import node


def main(*args):
    """Wrap the Node.js JavaScript runtime environment."""
    sys.exit(node.call(*args))


if __name__ == "__main__":
    main(*sys.argv[1:])
