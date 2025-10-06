#!/usr/bin/env python3


"""Wraps the Node.js JavaScript runtime environment."""


import sys

from .node import Node

if __name__ == "__main__":
    node = Node()
    sys.exit(node.main(*sys.argv[1:]))
