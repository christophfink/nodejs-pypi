#!/usr/bin/env python3


"""Wraps the Node.js JavaScript runtime environment."""


if __name__ == "__main__":
    import sys
    from .node import node
    sys.exit(node.main(*sys.argv[1:]))
