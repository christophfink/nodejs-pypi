#!/usr/bin/env python3


"""Test nodejs.base_command.BaseCommand."""


import pytest

import nodejs


class TestNodeJsBaseCommand:
    """Test nodejs.base_command.BaseCommand."""

    # Just the things that do not get touched when using it properly

    def test_not_implemented(self):
        """Test the exit code of node."""
        with pytest.raises(NotImplementedError):
            nodejs.base_command.BaseCommand().call()
