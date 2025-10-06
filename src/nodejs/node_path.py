#!/usr/bin/env python3


"""A pathlib.Path pointing to our copy of node."""


import importlib.resources
import pathlib

__all__ = ["NODE_PATH"]
__module__ = __name__.split(".", maxsplit=1)[0]
_NODE_PATH = "_node"


with importlib.resources.as_file(
    importlib.resources.files(__module__).joinpath(_NODE_PATH)
) as _node_path:
    NODE_PATH = pathlib.Path(_node_path).absolute()
