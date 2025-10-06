#!/usr/bin/env python3


"""Configuration and fixtures for testing nodejs-bin."""

import pathlib

import pytest


DATA_DIRECTORY = pathlib.Path(__file__).resolve().parent / "data"

TEST_SCRIPT_ARGS = DATA_DIRECTORY / "test_args.js"
TEST_SCRIPT_HELLO = DATA_DIRECTORY / "test_hello.js"


@pytest.fixture()
def script_file_args_path():
    """The file path to a script file that logs its own args to the console."""
    yield TEST_SCRIPT_ARGS


@pytest.fixture()
def script_file_hello_path():
    """The file path to a script file that logs "hello" to the console."""
    yield TEST_SCRIPT_HELLO


@pytest.fixture()
def node_path():
    """The file path to the node installation."""
    import nodejs.node_path

    yield nodejs.node_path.NODE_PATH
