#!/usr/bin/env python3

"""Wraps the Node.js JavaScript runtime environment."""


__version__ = "v24.0.1"
__all__ = ["__version__"]


import sys

try:
    if "-m" not in sys.argv:
        from .corepack import corepack
        from .node import node
        from .node_path import NODE_PATH as path
        from .npm import npm
        from .npx import npx

        node_version = __version__

        __all__ = [
            "corepack",
            "node",
            "npm",
            "npx",
            "path",
            "node_version",
            "__version__",
        ]

except ImportError:  # pragma: no cover
    pass
