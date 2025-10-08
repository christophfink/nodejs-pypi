# Node.js PyPI distribution

<!-- badges -->
[![stable version][stable-version-badge]][stable-version-link]
[![downloads][downloads-pypi-badge]][downloads-pypi-link]
[![Unit tests][test-status-badge]][test-status-link]
[![Coverage][coverage-badge]][coverage-link]
<br />


[Node.js][nodejs] is an open-source, cross-platform, back-end JavaScript runtime
environment that runs on the V8 engine and executes JavaScript code outside a
web browser. 

The [nodejs-bin][pypi] Python package redistributes Node.js so that it can be
used as a dependency of Python projects. With `nodejs-bin` you can call
`nodejs`, `npm`, `npx`, and `corepack` from both the [command
line](#command-line-usage) and a [Python API](#python-api-usage).

**Note: this is an unofficial Node.js distribution.** However, it repackages
official Node.js releases, only, which it acquires from one of the following
sources:

* Node.js official releases: <https://nodejs.org/en/download/releases/>
* Node.js ‘unofficial’ builds: <https://github.com/nodejs/unofficial-builds/>

**This package is intended for use within Python virtual environments and
containers, it should probably not be used for global installation.**

This PyPI distribution is provided by
<https://github.com/christophfink/nodejs-pypi>.


## Installation

`nodejs-bin` can be installed using `pip`, `uv`, `poetry`, or any other Python
package manager that can use the [PyPi package repository][pypi] or supports
`git+` or `https:` source URIs.

For example, to use `pip` to install `nodejs-bin` from PyPi, use:

```
pip install nodejs-bin
```

Similarly, to install the package directly from GitHub, into an [initialised `uv`
project][uv-project] directory, run:

```
uv add nodejs-bin@git+https://github.com/christophfink/nodejs-pypi.git
```

Finally, to add `nodejs-bin` to a [poetry project][poetry-project], using an
https package URL, run:

```
poetry add nodejs-bin@https://github.com/christophfink/nodejs-pypi/archive/refs/tags/v24.9.0.tar.gz
```


### Select a specific version of Node.js

`nodejs-bin`’s versioning aligns with Node.js’s. That means, when you install
`nodejs-bin` at version 24.9.0, it comes with Node.js 24.9.0. We strive to
publish new versions in a timely fashion, and always keep the [*current*,
*active (LTS)* and *maintenance* versions][nodejs-releases] up-to-date with
upstream releases.

You can pin your installation to a specific version by adding `==` and a version
string to the package name, or `@` and a tag name (equal to the version string)
to the `git+` package source URL. `https:` source URLs, at least in the form
described above, already contain a reference to a tag.

The following three commands are functionally equivalent:

```
pip install nodejs-bin==22.20.0
pip install nodejs-bin@git+https://github.com/christophfink/nodejs-bin.git@22.20.0
pip install nodejs-bin@https://github.com/christophfink/nodejs-pypi/archive/refs/tags/v22.20.0.tar.gz
```


### Command line shorthands

Optionally, `nodejs-bin` can provide the commands `node`, `npm`, and `npx`. 

**Warning:** these shorthands are not installed by default, as they collide with
potentially already installed Node.js (e.g., at a system-wide level). To avoid
collisions, it is preferred to run the modules’ `__main__`. To run `node`, for
install, use `python -m nodejs.node`, [see below](#command-line-usage).

There are, however, cases where using the Node.js binaries installed by
`nodejs-bin` outside Python is convenient. If you have read the warning above,
install shorthands for the command line utilities `node`, `npm`, and `npx` by
adding the optional dependency group `cmd` to the package identifier:

```
pip install 'nodejs-bin[cmd]'
```



## Quickstart

### Command line usage

To run `node` from the command line, use:

```
python -m nodejs.node
```

`npm`, `npx`, and `corepack` are available as `nodejs.npm`, `nodejs.npx`, and
`nodejs.corepack`, respectively:

```
python -m nodejs.npm

python -m nodejs.npx

python -m nodejs.corepack
```

*For legacy reasons, the root module of the package can be called, as well. It
wraps `node`. <br/>
That means, `python -m nodejs` is equivalent to `python -m nodejs.node`.*


### Python API Usage

`node-bin` has a simple Python API that wraps the Node.js command line in a
[Python `subprocess`][python-docs-subprocess].

For `node`, `npm`, `npx`, and `corepack` there are `.call()`, `.run()` and
`.Popen()` methods that match the respective `subprocess` methods.


#### `node.call()`, `npm.call()`, `npx.call()`, and `corepack.call()`

To run Node.js from a Python program and return the exit code:

```python
from nodejs import node, npm, npx, corepack

# Run Node.js and return the exit code.
node.call('script.js', 'arg1', …, **kwargs)

# Run npm and return the exit code.
npm.call('command', 'arg1', …, **kwargs)

# Run npx and return the exit code.
npx.call('command', 'arg1', …, **kwargs)

# Run corepack and return the exit code.
corepack.call('command', 'arg1', …, **kwargs)
```

The `call(args, **kwargs)` functions wrap
[`subprocess.call()`][python-docs-subprocess-call], pass all `kwargs` through to
`subprocess.call` and return the exit codes of the processes.


#### `node.run()`, `npm.run()`, `npx.run()`, `corepack.run()`

To run Node.js from a Python program and return a
[`CompletedProcess`][python-docs-subprocess-completed-process] object:

```python
from nodejs import node, npm, npx, corepack

# Run Node.js and return a CompletedProcess object.
node.run('script.js', 'arg1', …, **kwargs)

# Run npm and return a CompletedProcess object.
npm.run('command', 'arg1', …, **kwargs)

# Run npx and return a CompletedProcess object.
npx.run('command', 'arg1', …, **kwargs)

# Run corepack and return a CompletedProcess object.
corepack.run('command', 'arg1', …, **kwargs)
```

The `call(args, **kwargs)` functions wrap
[`subprocess.run()`][python-docs-subprocess-run], pass all `kwargs` through to
`subprocess.run` and return the exit codes of the processes.



#### `node.Popen()`, `npm.Popen()`, `npx.Popen()`, and `corepack.Popen()`

Additionally, to start a Node.js process and return a [`subprocess.Popen`
object][python-docs-subprocess-popen-objects], you can use the `Popen(args,
**kwargs)` functions:

```python
from nodejs import node, npm, npx, corepack

# Start Node.js and return the Popen object.
node_process = node.Popen('script.js', 'arg1', …, **kwargs)

# Start npm and return the Popen object.
npm_process = npm.Popen('command', 'arg1', …, **kwargs)

# Start npx and return the Popen object.
npx_process = npx.Popen('command', 'arg1', …, **kwargs)

# Start corepack and return the Popen object.
corepack_process = corepack.Popen('command', 'arg1', …, **kwargs)
```


The `call(args, **kwargs)` functions wrap
[`subprocess.Popen()`][python-docs-subprocess-Popen], pass all `kwargs` through
to `subprocess.Popen` and return [`Popen` objects][python-docs-subprocess-popen-objects].



#### Metadata

Finally, the `nodejs` module exposes some attributes that contain convenient
information about the packaged Node.js:

`nodejs.node_version`
: the version of Node.js that is installed.

`nodejs.path`
: the path to the Node.js executable.


## Versions

nodejs-bin offers Node.js *current*, *active (LTS, long-term support)*, and
*maintenance* versions. See the [Node.js Documentation][nodejs-releases] for
more information.

The full list of versions is available on PyPI can be found here:
<https://pypi.org/project/nodejs-bin/#history>


## Licenses

Node.js is licensed under the [Node.js license][nodejs-license].

This Python package is licensed under an [MIT license][nodejs-pypi-license].



<!-- links -->
[coverage-badge]: https://codecov.io/gh/christophfink/nodejs-pypi/branch/main/graph/badge.svg?token=emlBDgnStv
[coverage-link]: https://codecov.io/gh/christophfink/nodejs-pypi
[downloads-pypi-badge]: https://static.pepy.tech/personalized-badge/nodejs-bin?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads
[downloads-pypi-link]: https://pypi.org/project/nodejs-bin
[stable-version-badge]: https://img.shields.io/pypi/v/nodejs-bin?label=Stable
[stable-version-link]: https://github.com/christophfink/nodejs-pypi/releases
[test-status-badge]: https://github.com/christophfink/nodejs-pypi/actions/workflows/test.yml/badge.svg
[test-status-link]: https://github.com/christophfink/nodejs-pypi/actions/workflows/test.yml


[nodejs]: https://nodejs.org/
[nodejs-license]: https://raw.githubusercontent.com/nodejs/node/master/LICENSE
[nodejs-releases]: https://nodejs.org/en/about/releases/
[nodejs-pypi-license]: LICENSE
[poetry-project]: https://python-poetry.org/docs/basic-usage/#project-setup
[pypi]: https://pypi.org/project/nodejs-bin/
[python-docs-subprocess]: https://docs.python.org/3/library/subprocess.html
[python-docs-subprocess-call]: https://docs.python.org/3/library/subprocess.html#subprocess.call
[python-docs-subprocess-run]: https://docs.python.org/3/library/subprocess.html#subprocess.run
[python-docs-subprocess-popen]: https://docs.python.org/3/library/subprocess.html#subprocess.Popen
[python-docs-subprocess-completed-process]: https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess
[python-docs-subprocess-popen-objects]: https://docs.python.org/3/library/subprocess.html#popen-objects
[uv-project]: https://docs.astral.sh/uv/#projects
