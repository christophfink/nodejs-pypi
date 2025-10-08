#!/usr/bin/env python3


"""Test nodejs.maybe_script.MaybeScript."""


import pytest

import nodejs


class TestNodeJsMaybeScript:
    """Test nodejs.maybe_script.MaybeScript."""

    # Just the things that do not get touched when using it properly

    def test_not_implemented(self):
        """Test the exit code of node."""
        with pytest.raises(NotImplementedError):
            nodejs.maybe_script.MaybeScript().call()
    
    def test_not_implemented_on_poorly_defined_children(self):
        class _PoorlyDefinedChild(nodejs.maybe_script.MaybeScript):
            pass

        with pytest.raises(NotImplementedError):
            _PoorlyDefinedChild().call()

        class _PoorlyDefinedChild(nodejs.maybe_script.MaybeScript):
            _script_name = "foobar"

        with pytest.raises(NotImplementedError):
            _PoorlyDefinedChild().call()
        
        class _PoorlyDefinedChild(nodejs.maybe_script.MaybeScript):
            _command_name = "foobar"

        with pytest.raises(NotImplementedError):
            _PoorlyDefinedChild().call()
