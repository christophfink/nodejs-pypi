#!/usr/bin/env python3


"""Test nodejs.corepack."""


import re

import pytest

import nodejs


class TestNodeJsCorepack:
    """Test nodejs.corepack."""

    def test_exit_code_success(self):
        """Test the exit code of node."""
        exit_code = nodejs.corepack.call("--version")
        assert exit_code == 0

    def test_version(self, capfd):
        """Test the output of corepack --version."""
        nodejs.corepack.call("--version")
        stdout, _ = capfd.readouterr()
        assert re.match(r"[0-9]+\.[0-9]+\.[0-9]+", stdout.strip())

    def test_missing_executable(self, node_path):
        """Temporarily remove corepack executable."""
        try:
            # rename node executable
            for command in [
                node_path / "bin" / "corepack",
                node_path / "corepack.cmd",
            ]:
                try:
                    command.rename(command.with_suffix(".disabled"))
                except FileNotFoundError:
                    pass

            # clear functools.cached_property
            nodejs.corepack.__dict__.pop("_command", None)
            nodejs.corepack.__dict__.pop("_script_name", None)

            # re-evaluate executable path
            with pytest.raises(
                RuntimeError, match="Could not find corepack executable"
            ):
                _ = nodejs.corepack._command
                _ = nodejs.corepack._script_name
        finally:
            # restore original node executables
            for command in [
                node_path / "bin" / "corepack",
                node_path / "corepack.cmd",
            ]:
                try:
                    command.with_suffix(".disabled").rename(command)
                except FileNotFoundError:
                    pass

            # clear functools.cached_property
            nodejs.node.__dict__.pop("_command", None)
