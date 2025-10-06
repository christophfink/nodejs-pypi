#!/usr/bin/env python3


"""Test nodejs.npx."""


import re

import pytest

import nodejs


class TestNodeJsNpx:
    """Test nodejs.npx."""

    def test_exit_code_success(self):
        """Test the exit code of node."""
        exit_code = nodejs.npx.call("--version")
        assert exit_code == 0

    def test_version(self, capfd):
        """Test the output of npx --version."""
        nodejs.npx.call("--version")
        stdout, _ = capfd.readouterr()
        assert re.match(r"[0-9]+\.[0-9]+\.[0-9]+", stdout.strip())

    def test_missing_executable(self, node_path):
        """Temporarily remove npx executable."""
        try:
            # rename node executable
            for command in [
                node_path / "bin" / "npx",
                node_path / "npx.cmd",
            ]:
                try:
                    command.rename(command.with_suffix(".disabled"))
                except FileNotFoundError:
                    pass

            # clear functools.cached_property
            nodejs.npx.__dict__.pop("_command", None)
            nodejs.npx.__dict__.pop("_script_name", None)

            # re-evaluate executable path
            with pytest.raises(RuntimeError, match="Could not find npx executable"):
                _ = nodejs.npx._command
                _ = nodejs.npx._script_name
        finally:
            # restore original node executables
            for command in [
                node_path / "bin" / "npx",
                node_path / "npx.cmd",
            ]:
                try:
                    command.with_suffix(".disabled").rename(command)
                except FileNotFoundError:
                    pass

            # clear functools.cached_property
            nodejs.node.__dict__.pop("_command", None)
