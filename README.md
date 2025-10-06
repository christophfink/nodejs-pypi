# Node.js PyPI distribution

<!-- badges -->
[![stable version][stable-version-badge]][stable-version-link]
[![downloads][downloads-pypi-badge]][downloads-pypi-link]
<br />
[![Unit tests][test-status-badge]][test-status-link]
[![Coverage][coverage-badge]][coverage-link]
<br />


[Node.js][nodejs] is an open-source, cross-platform, back-end JavaScript runtime
environment that runs on the V8 engine and executes JavaScript code outside a
web browser. 

The [nodejs-bin][pypi] Python package redistributes Node.js so that it can be
used as a dependency of Python projects. With `nodejs-bin` you can call
`nodejs`, `npm` and `npx` from both the [command line](#command-line-usage) and
a [Python API](#python-api-usage).

**Note: this is an unofficial Node.js distribution.** However, it _does_ use
only official bits distributed by the official NodeJS maintainers from one of
the following sources:

* NodeJS official releases: <https://nodejs.org/en/download/releases/>
* NodeJS ‘unofficial’ builds: <https://github.com/nodejs/unofficial-builds/>

**This is intended for use within Python virtual environments and containers, it
should probably not be used for global installation.**

This PyPI distribution is provided by
<https://github.com/samwillis/nodejs-pypi>.


## Install

To install, use pip:

```shell
pip install nodejs-bin
```

By default the command line `node`, `npm` and `npx` commands are not installed
to prevent collisions with already installed Node.js versions. To install them:

```shell
pip install 'nodejs-bin[cmd]'
```

You can specify the Node.js version to install with:

```shell
pip install nodejs-bin==<version>

# Example:
pip install nodejs-bin==24.9.0
```

Command Line Usage
------------------

To run Node.js from the command line, use:

```shell
python -m nodejs
```

`npm` and `npx` are also available as `nodejs.npm` and `nodejs.npx`:

```shell
python -m nodejs.npm
python -m nodejs.npx
```

If you installed the optional command line commands with `pip install 'nodejs-bin[cmd]'` (see above), you can use them directly from the command line as you would normally with Node.js:

```shell
node
npm
npx
```

Python API Usage
----------------

`node-bin` has a simple Python API that wraps the Node.js command line with the
[Python `subprocess`][python-docs-subprocess].

For `node`, `npm` and `npx` there are `.call()`, `.run()` and `.Popen()` methods
that match the equivalent `subprocess` methods.

To run Node.js from a Python program and return the exit code:

```python
from nodejs import node, npm, npx

# Run Node.js and return the exit code.
node.call(['script.js', 'arg1', ...], **kwargs)

# Run npm and return the exit code.
npm.call(['command', 'arg1', ...], **kwargs)

# Run npx and return the exit code.
npx.call(['command', 'arg1', ...], **kwargs)
```

The `call(args, **kwargs)` functions wrap
[`subprocess.call()`][python-docs-subprocess-call], passes though all `kwargs`
and returns the exit code of the process.

To run Node.js from a Python program and return a
[`CompletedProcess`][python-docs-subprocess-completed-process] object:

```python
from nodejs import node, npm, npx

# Run Node.js and return the exit code.
node.run(['script.js', 'arg1', ...], **kwargs)

# Run npm and return the exit code.
npm.run(['command', 'arg1', ...], **kwargs)

# Run npx and return the exit code.
npx.run(['command', 'arg1', ...], **kwargs)
```

The `run(args, **kwargs)` functions wrap
[`subprocess.run()`][python-docs-subprocess-run], passes though all `kwargs` and
returns a `CompletedProcess`.

Additionally, to start a Node.js process and return a `subprocess.Popen` object, you can use the `Popen(args, **kwargs)` functions:

```python
from nodejs import node, npm, npx

# Start Node.js and return the Popen object.
node_process = node.Popen(['script.js', 'arg1', ...], **kwargs)

# Start npm and return the Popen object.
npm_process = npm.Popen(['command', 'arg1', ...], **kwargs)

# Start npx and return the Popen object.
npx_process = npx.Popen(['command', 'arg1', ...], **kwargs)
```

The `Popen(args, **kwargs)` functions wrap
[`subprocess.Popen()`][python-docs-subprocess-popen], passes though all `kwargs`
and returns a [`Popen` object][python-docs-subprocess-popen-objects].

The `nodejs.node` api is also available as `nodejs.run` and `nodejs.call` and
`nodejs.Popen`.

Finally, there are a number of convenient attributes on the `nodejs` module:

  * `nodejs.node_version`: the version of Node.js that is installed.
  * `nodejs.path`: the path to the Node.js executable.


## Versions

nodejs-bin offers Node.js *Current* and *LTS* (long-term support) versions. See
the [Node.js Documentation][nodejs-releases] for more information.

The full list of versions is available on PyPI is here:
<https://pypi.org/project/nodejs-bin/#history>


## Licenses

Node.js is licensed under the [Node.js license][nodejs-license].
This Python package is licensed under a [MIT license][nodejs-pypi-license].



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
[pypi]: https://pypi.org/project/nodejs-bin/
[python-docs-subprocess]: https://docs.python.org/3/library/subprocess.html
[python-docs-subprocess-call]: https://docs.python.org/3/library/subprocess.html#subprocess.call
[python-docs-subprocess-run]: https://docs.python.org/3/library/subprocess.html#subprocess.run
[python-docs-subprocess-popen]: https://docs.python.org/3/library/subprocess.html#subprocess.Popen
[python-docs-subprocess-completed-process]: https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess
[python-docs-subprocess-popen-objects]: https://docs.python.org/3/library/subprocess.html#popen-objects
