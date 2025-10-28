#!/usr/bin/env python3


"""Test nodejs.__main__."""


import subprocess
import sys

import pytest

import nodejs


class TestNodeJsMain:
    """Test nodejs.__main__."""

    def test_node_exit_code_success(self):
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

    def test_node_exit_code_error(self):
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

    def test_main_version(self, capfd):
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

    def test_main_eval_stdout(self, capfd):
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

    def test_main_eval_stderr(self, capfd):
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

    def test_main_script_hello(self, capfd, script_file_hello_path):
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
    def test_main_script_args(self, capfd, script_file_args_path, args):
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

    def test_node_version(self, capfd):
        """Test the output of node --version."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs.node",
                "--version",
            ]
        )
        stdout, _ = capfd.readouterr()
        assert exit_code == 0
        assert stdout.strip() == nodejs.__version__

    def test_node_eval_stdout(self, capfd):
        """Test whether passed-in code is run."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs.node",
                "--eval",
                'console.log("hello")',
            ]
        )
        stdout, _ = capfd.readouterr()
        assert exit_code == 0
        assert stdout.strip() == "hello"

    def test_node_eval_stderr(self, capfd):
        """Test whether passed-in code is run."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs.node",
                "--eval",
                'console.error("hello")',
            ]
        )
        _, stderr = capfd.readouterr()
        assert exit_code == 0
        assert stderr.strip() == "hello"

    def test_node_script_hello(self, capfd, script_file_hello_path):
        """Test running a script file."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs.node",
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
    def test_node_script_args(self, capfd, script_file_args_path, args):
        """Test running a script file."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs.node",
                script_file_args_path,
                *args,
            ]
        )
        stdout, _ = capfd.readouterr()
        assert exit_code == 0
        assert stdout.strip() == args[0]

    def test_npm_exit_code_success(self):
        """Test the exit code of node.__main__."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs.npm",
                "--version",
            ]
        )
        assert exit_code == 0

    def test_npx_exit_code_success(self):
        """Test the exit code of node.__main__."""
        exit_code = subprocess.call(
            [
                sys.executable,
                "-m",
                "nodejs.npx",
                "--version",
            ]
        )
        assert exit_code == 0

    def test_node_entry_point(self):
        """Test the node entry point."""
        exit_code = subprocess.call(
            [
                "node",
                "--version",
            ]
        )
        assert exit_code == 0

    def test_npm_entry_point(self):
        """Test the npm entry point."""
        exit_code = subprocess.call(
            [
                "npm",
                "--version",
            ]
        )
        assert exit_code == 0

    def test_npx_entry_point(self):
        """Test the npx entry point."""
        exit_code = subprocess.call(
            [
                "npx",
                "--version",
            ]
        )
        assert exit_code == 0

    def test_node_main_function(self):
        """Test the node main() function."""
        from nodejs.node import main

        sys_argv = sys.argv
        sys.argv = [sys.argv[0]] + ["--version"]

        try:
            main()
        except SystemExit as exception:
            if exception.code != 0:
                raise
        finally:
            sys.argv = sys_argv

    def test_npm_main_function(self):
        """Test the npm main() function."""
        from nodejs.npm import main

        sys_argv = sys.argv
        sys.argv = [sys.argv[0]] + ["--version"]

        try:
            main()
        except SystemExit as exception:
            if exception.code != 0:
                raise
        finally:
            sys.argv = sys_argv

    def test_npx_main_function(self):
        """Test the npx main() function."""
        from nodejs.npx import main

        sys_argv = sys.argv
        sys.argv = [sys.argv[0]] + ["--version"]

        try:
            main()
        except SystemExit as exception:
            if exception.code != 0:
                raise
        finally:
            sys.argv = sys_argv
