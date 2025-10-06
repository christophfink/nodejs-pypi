#!/usr/bin/env python3


"""A pathlib.Path pointing to our copy of node."""


import pathlib

try:
    import importlib.resources as importlib_resources
except ImportError:
    import importlib_resources


__all__ = ["NODE_PATH"]
__module__ = __name__.split(".", maxsplit=1)[0]
_NODE_PATH = "_node"


with importlib_resources.as_file(
    importlib_resources.files(__module__).joinpath(_NODE_PATH)
) as _node_path:
    NODE_PATH = pathlib.Path(_node_path).absolute()
