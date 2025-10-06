#!/usr/bin/env python3


"""Test nodejs.__main__."""


import subprocess
import sys

import pytest

import nodejs


class TestNodeJsMain:
    """Test nodejs.__main__."""

    def test_exit_code_success(self):
        """Test the exit code of node.__main__."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs",
                "--version",
            ]
        )
        assert exit_code == 0

    def test_exit_code_error(self):
        """Test the exit code of node.__main__."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs",
                "--eval",
                "process.exit(1)",
            ]
        )
        assert exit_code == 1

    def test_main_function(self):
        """Test the exit code of node.__main__."""
        import nodejs.__main__

        try:
            nodejs.__main__.main("--version")
        except SystemExit as exception:
            if exception.code != 0:
                raise

    def test_version(self, capfd):
        """Test the output of node --version."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs",
                "--version",
            ]
        )
        stdout, _ = capfd.readouterr()
        assert exit_code == 0
        assert stdout.strip() == nodejs.__version__

    def test_eval_stdout(self, capfd):
        """Test whether passed-in code is run."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs",
                "--eval",
                'console.log("hello")',
            ]
        )
        stdout, _ = capfd.readouterr()
        assert exit_code == 0
        assert stdout.strip() == "hello"

    def test_eval_stderr(self, capfd):
        """Test whether passed-in code is run."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs",
                "--eval",
                'console.error("hello")',
            ]
        )
        _, stderr = capfd.readouterr()
        assert exit_code == 0
        assert stderr.strip() == "hello"

    def test_script_hello(self, capfd, script_file_hello_path):
        """Test running a script file."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs",
                script_file_hello_path,
            ]
        )
        stdout, _ = capfd.readouterr()
        assert exit_code == 0
        assert stdout.strip() == "hello"

    @pytest.mark.parametrize(
        ("args",),
        (
            (["hello"],),
            (["a", "b"],),
            (["--foo=bar"]),
        ),
    )
    def test_script_args(self, capfd, script_file_args_path, args):
        """Test running a script file."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs",
                script_file_args_path,
                *args,
            ]
        )
        stdout, _ = capfd.readouterr()
        assert exit_code == 0
        assert stdout.strip() == args[0]
