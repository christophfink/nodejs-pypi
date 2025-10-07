# Development notes

This repository contains the Python package `nodejs-bin` that re-packages
[Node.js][nodejs] releases that can be distributed in source (`sdist`) and
binary (`wheel`) formats. 

This document is intended to inform maintainers, see the [README][readme] for
rationale and usage instructions.

Previous versions of the packaging backend for `nodejs-bin` were based on the
work of the creators of the [Zig language][ziglang], see [the
original][zig-pypi].

The current version is a rewrite from scratch that focusses on maintainability:
it does not generated code on the fly, and relies on an [in-tree build-backend,
as specified in PEP517][pep517-intree-build-backend] to download, extract and
include the relevant Node.js distribution in the Python package.


## Requirements

The package is fully compliant to the specifications set forward in [PEP518 and
PEP621][packaging-pyproject]. This means the `pyproject.toml` contains all
information to build this package with any compliant build toolchain, e.g.,
[`build`][python-build] or plain old [`pip`][python-pip]. These tools then
create an isolated environment in which they install all other build-time
requirements before building the package.


## Building

With [`build`][python-build] available, navigate to the source directory and run 

```
python -m build
```

The build backend (in [`/build_backend/`][build-backend]) determines the local
architecture and downloads the appropriate Node.js package, which it then
includes in the wheel.

If you intend to package for a different architecture, pass in the argument
`--config-setting target-platform="TARGET_PLATFORM"`, where `TARGET_PLATFORM` is
either a Python [platform compatibility tag][python-platform-tag] or a Node.js
[platform identifier][nodejs-platforms].

```
python -m build --wheel --config-setting target-platform="win-x64"
```

As architectures are changing over time, and the set of available options
depends on availability from both projects, no definite list can be decided,
check [`build_backend/platforms.py`][build-backend-platforms] for a current
list.


## Running unit tests

To run unit tests, navigate to the source directory, install the `tests` set of
optional dependencies and run `python -m pytest`. You might want to do all of
this inside a [virtual environment][python-venv].

```
pip install .[tests]
python -m pytest
```


## Continuous Integration/GitHub actions build and test toolchain

This GitHub repository is set up to run unit tests on each pull request, on a
variety of operating systems and architectures, to ensure changes do not break
existing code.

Whenever a (protected) version tag in the format `v0.0.0` is pushed to the
`main` branch, wheels are built and published to PyPi if tests pass
successfully and maintainers approve of the changeset.


<!-- links -->
[build-backend-platforms]: build_backend/platforms.py
[build-backend]: build_backend/
[nodejs-platforms]: https://github.com/nodejs/node/blob/main/BUILDING.md#platform-list
[nodejs]: https://nodejs.org/
[packaging-pyproject]: https://packaging.python.org/en/latest/specifications/pyproject-toml/
[pep517-intree-build-backend]: https://peps.python.org/pep-0517/#build-backend-interface
[python-build]: https://build.pypa.io/en/stable/index.html
[python-pip]: https://pip.pypa.io/en/stable/
[python-platform-tag]: https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/
[python-venv]: https://docs.python.org/3/library/venv.html
[readme]: README.md
[zig-pypi]: https://github.com/ziglang/zig-pypi
[ziglang]: https://ziglang.org/
