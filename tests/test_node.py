#!/usr/bin/env python3


"""Test nodejs.node."""


import pytest

import nodejs


class TestNodeJsNode:
    """Test nodejs.node."""

    def test_exit_code_success(self):
        """Test the exit code of node."""
        exit_code = nodejs.node.call("--version")
        assert exit_code == 0

    def test_exit_code_success_run(self):
        """Test the exit code of node."""
        exit_code = nodejs.node.run("--version").returncode
        assert exit_code == 0

    def test_exit_code_success_popen(self):
        """Test the exit code of node."""
        exit_code = nodejs.node.Popen("--version").wait()
        assert exit_code == 0

    def test_exit_code_success_arglist(self):
        """Test the exit code of node."""
        exit_code = nodejs.node.call(["--version"])
        assert exit_code == 0

    def test_exit_code_success_run_arglist(self):
        """Test the exit code of node."""
        exit_code = nodejs.node.run(["--version"]).returncode
        assert exit_code == 0

    def test_exit_code_success_popen_arglist(self):
        """Test the exit code of node."""
        exit_code = nodejs.node.Popen(["--version"]).wait()
        assert exit_code == 0

    def test_exit_code_error(self):
        """Test the exit code of node."""
        exit_code = nodejs.node.call("--eval", "process.exit(1)")
        assert exit_code == 1

    def test_version(self, capfd):
        """Test the output of node --version."""
        nodejs.node.call("--version")
        stdout, _ = capfd.readouterr()
        assert stdout.strip() == nodejs.__version__

    def test_eval_stdout(self, capfd):
        """Test whether passed-in code is run."""
        nodejs.node.call("--eval", 'console.log("hello")')
        stdout, _ = capfd.readouterr()
        assert stdout.strip() == "hello"

    def test_eval_stderr(self, capfd):
        """Test whether passed-in code is run."""
        nodejs.node.call("--eval", 'console.error("hello")')
        _, stderr = capfd.readouterr()
        assert stderr.strip() == "hello"

    def test_script_hello(self, capfd, script_file_hello_path):
        """Test running a script file."""
        nodejs.node.call(script_file_hello_path)
        stdout, _ = capfd.readouterr()
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
        nodejs.node.call(script_file_args_path, *args)
        stdout, _ = capfd.readouterr()
        assert stdout.strip() == args[0]

    def test_missing_executable(self, node_path):
        """Temporarily remove node executable."""
        try:
            # rename node executable
            for command in [
                node_path / "bin" / "node",
                node_path / "node.exe",
            ]:
                try:
                    command.rename(command.with_suffix(".disabled"))
                except FileNotFoundError:
                    pass

            # clear functools.cached_property
            nodejs.node.__dict__.pop("_command", None)

            # re-evaluate executable path
            with pytest.raises(RuntimeError, match="Could not find node executable"):
                _ = nodejs.node._command
        finally:
            # restore original node executables
            for command in [
                node_path / "bin" / "node",
                node_path / "node.exe",
            ]:
                try:
                    command.with_suffix(".disabled").rename(command)
                except FileNotFoundError:
                    pass

            # clear functools.cached_property
            nodejs.node.__dict__.pop("_command", None)
