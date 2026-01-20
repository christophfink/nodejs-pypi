#!/usr/bin/env python3


"""Test nodejs.npm."""

import re

import pytest

import nodejs

from .working_directory import WorkingDirectory


class TestNodeJsNpm:
    """Test nodejs.npm."""

    def test_exit_code_success(self):
        """Test the exit code of node."""
        exit_code = nodejs.npm.call("--version")
        assert exit_code == 0

    def test_version(self, capfd):
        """Test the output of npm --version."""
        nodejs.npm.call("--version")
        stdout, _ = capfd.readouterr()
        assert re.match(r"[0-9]+\.[0-9]+\.[0-9]+", stdout.strip())

    def test_install(self, capfd, tmp_path):
        """Test whether npm installs packages successfully."""
        with WorkingDirectory(tmp_path):

            nodejs.npm.call("init", "-y")
            assert (tmp_path / "package.json").exists()

            nodejs.npm.call("install", "is-even")
            assert (tmp_path / "node_modules" / "is-even").exists()

            _ = capfd.readouterr()

            nodejs.node.call("--eval", 'console.log(require("is-even")(42))')
            stdout, _ = capfd.readouterr()
            assert stdout.strip() == "true"

            nodejs.node.call("--eval", 'console.log(require("is-even")(43))')
            stdout, _ = capfd.readouterr()
            assert stdout.strip() == "false"

    def test_missing_executable(self, node_path):
        """Temporarily remove npm executable."""
        try:
            # rename node executable
            for command in [
                node_path / "bin" / "npm",
                node_path / "npm.cmd",
            ]:
                try:
                    command.rename(command.with_suffix(".disabled"))
                except FileNotFoundError:
                    pass

            # clear functools.cached_property
            nodejs.npm.__dict__.pop("_command", None)
            nodejs.npm.__dict__.pop("_script_name", None)

            # re-evaluate executable path
            with pytest.raises(RuntimeError, match="Could not find npm executable"):
                _ = nodejs.npm._command
                _ = nodejs.npm._script_name
        finally:
            # restore original node executables
            for command in [
                node_path / "bin" / "npm",
                node_path / "npm.cmd",
            ]:
                try:
                    command.with_suffix(".disabled").rename(command)
                except FileNotFoundError:
                    pass

            # clear functools.cached_property
            nodejs.node.__dict__.pop("_command", None)
