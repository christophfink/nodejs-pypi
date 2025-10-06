#!/usr/bin/env python3

"""Wraps the Node.js JavaScript runtime environment."""


__version__ = "v24.9.0"
__all__ = []

try:
    from .corepack import Corepack
    from .node import Node
    from .npm import Npm
    from .npx import Npx

    corepack = Corepack()
    node = Node()
    npm = Npm()
    npx = Npx()

    __all__ = [
        "corepack",
        "node",
        "npm",
        "npx",
    ]
except ImportError:  # pragma: no cover
    pass
