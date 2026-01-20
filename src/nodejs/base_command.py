#!/usr/bin/env python3


"""A base class for the commands exposed by nodejs."""

import subprocess


class BaseCommand:
    """A base class for the commands exposed by nodejs."""

    @property
    def _command(self):
        raise NotImplementedError(
            "Do not use BaseCommand directly. "
            "Rather, inherit from it, and define the child class’ _command"
        )

    def call(self, *args, **kwargs):
        """Run with the semantics of subprocess.call."""
        if len(args) == 1 and isinstance(args[0], list):
            args = args[0]
        return subprocess.call(self._command + list(args), **kwargs)

    def run(self, *args, **kwargs):
        """Run with the semantics of subprocess.run."""
        if len(args) == 1 and isinstance(args[0], list):
            args = args[0]
        return subprocess.run(self._command + list(args), **kwargs)

    def Popen(self, *args, **kwargs):
        """Run with the semantics of subprocess.Popen."""
        if len(args) == 1 and isinstance(args[0], list):
            args = args[0]
        return subprocess.Popen(self._command + list(args), **kwargs)
