[![Build Status](https://travis-ci.com/timhourigan/gh-playground.svg?branch=master)](https://travis-ci.com/timhourigan/gh-playground)
[![Coverage Status](https://coveralls.io/repos/github/timhourigan/gh-playground/badge.svg?branch=master)](https://coveralls.io/github/timhourigan/gh-playground?branch=master)

### Playground

A playground repository for testing Github, [Travis CI](https://travis-ci.com) and [Coveralls](https://coveralls.io/).

#### Python Testing

The project contains a Python module (*read_travis.py*) with sample unit tests (*test_read_travis.py*), written using the [pytest](https://docs.pytest.org/en/latest/) framework.

The tests and [Flake8](https://flake8.readthedocs.io/en/latest/index.html) are executed by Travis CI, with code coverage reported using Coveralls.

| File                | Content                                                                           |
|:--------------------|:----------------------------------------------------------------------------------|
| .coveragerc         | Contains a list of ignores (omits, excludes) for the code coverage check.         |
| .gitignore          | git ignore list.                                                                  |
| .travis.yml         | Travis CI configuration.                                                          |
| conftest.py         | Currently unused, could contain common test fixtures or imports.                  |
| Makefile            | Makefile to execute tests.                                                        |
| LICENSE             | Repository license.                                                               |
| read_travis.py      | Dummy Python module. Creates an object based on the contents of *.travis.yml*.    |
| README.md           | This file.                                                                        |
| Pipfile             | Python pipenv requirements file, containing a list of the needed Python packages. |
| Pipfile.lock        | Python pipenv lock file.                                                          |
| setup.cfg           | Contains pytest and flake8 default settings.                                      |
| test_read_travis.py | Sample unit tests.                                                                |

#### Usage - Pipenv on Ubuntu/Debian

```bash
# Install pip and pipenv locally
$ sudo apt install python3-pip
# This assumes PATH includes ~/.local/bin
$ pip install --user pipenv

# Setup the environment
$ pipenv sync --dev
$ pipenv shell

# Run tests and coverage locally
$ make test
```

#### Continuous Integration

Useful links for pytest, code coverage, Travis CI and Coveralls:

* [Robin Andeer - How I test my code](http://www.robinandeer.com/blog/2016/06/22/how-i-test-my-code-part-3/)
* [I Love Symposia - Continuous integration in Python](https://ilovesymposia.com/2014/10/01/continuous-integration-0-automated-tests-with-pytest/)
