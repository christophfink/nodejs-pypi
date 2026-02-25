#!/usr/bin/env python3

"""Wraps the Node.js JavaScript runtime environment."""

__version__ = "v25.7.0"

__all__ = ["__version__"]


import sys

try:
    if "-m" not in sys.argv:
        from .node import node
        from .node_path import NODE_PATH as path
        from .npm import npm
        from .npx import npx

        node_version = __version__

        __all__ = [
            "node",
            "npm",
            "npx",
            "path",
            "node_version",
            "__version__",
        ]

except ImportError:  # pragma: no cover
    pass
