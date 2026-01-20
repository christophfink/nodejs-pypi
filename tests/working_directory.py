#!/usr/bin/env python3


"""A working directory context manager."""

import os
import pathlib


class WorkingDirectory:
    """Context manager to change working directory."""

    def __init__(self, working_directory):
        """Context manager to change working directory."""
        self._working_directory = pathlib.Path(working_directory)
        self._original_working_directory = None

    def __enter__(self):
        """Continue working in a new directory."""
        self._original_working_directory = pathlib.Path.cwd()
        os.chdir(self._working_directory)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Return to the original working directory."""
        os.chdir(self._original_working_directory)
