#!/usr/bin/env python3


"""Test nodejs.npm."""


import re

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
