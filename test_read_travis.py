#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# Imports
#
########################################################################

import pytest

from read_travis import Configuration

########################################################################
#
# Defines
#
########################################################################

UNKNOWN_LANGUAGE = 'Unknown'

DEFAULT_LANGUAGE = 'python'
DEFAULT_PYTHON_LIST = ['3.6']
DEFAULT_INSTALL_LIST = ['pip install pipenv', 'pipenv sync --dev']
DEFAULT_SCRIPT_LIST = ['pipenv run py.test', 'pipenv run flake8', 'pipenv run black .']

BAD_CONFIGURATION_FILE = '.bad.yml'

NOT_A_STRING = 12345
NOT_A_LIST = "Not a list"

########################################################################
#
# Test Fixtures
#
########################################################################


@pytest.fixture
def empty_configuration():
    """Empty configuration object"""
    return Configuration(language=UNKNOWN_LANGUAGE, python=list(),
                         install=list(), script=list())


@pytest.fixture
def default_configuration():
    """Default configuration object"""
    return Configuration.import_cfg()


@pytest.fixture
def bad_configuration():
    """Bad configuration object"""
    return Configuration.import_cfg(filename=BAD_CONFIGURATION_FILE)

########################################################################
#
# Tests
#
########################################################################


# Empty tests
def test_language_empty(empty_configuration):
    assert empty_configuration.language == UNKNOWN_LANGUAGE


def test_python_empty(empty_configuration):
    assert empty_configuration.python == list()


def test_install_empty(empty_configuration):
    assert empty_configuration.install == list()


def test_script_empty(empty_configuration):
    assert empty_configuration.script == list()


# Read default tests
def test_language_default(default_configuration):
    assert default_configuration.language == DEFAULT_LANGUAGE


def test_python_default(default_configuration):
    assert default_configuration.python == DEFAULT_PYTHON_LIST


def test_install_default(default_configuration):
    assert default_configuration.install == DEFAULT_INSTALL_LIST


def test_script_default(default_configuration):
    assert default_configuration.script == DEFAULT_SCRIPT_LIST


def test_repr_default(default_configuration):
    assert repr(default_configuration) == \
        'Configuration({!r}, {!r}, {!r}, {!r})'.format(DEFAULT_LANGUAGE,
                                                       DEFAULT_PYTHON_LIST,
                                                       DEFAULT_INSTALL_LIST,
                                                       DEFAULT_SCRIPT_LIST)


# Bad Configuration
def test_bad_configuration(bad_configuration):
    assert bad_configuration.language == UNKNOWN_LANGUAGE
    assert bad_configuration.python == list()
    assert bad_configuration.install == list()
    assert bad_configuration.script == list()


def test_bad_language(default_configuration):
    with pytest.raises(TypeError):
        default_configuration.language = NOT_A_STRING


def test_bad_python(default_configuration):
    with pytest.raises(TypeError):
        default_configuration.python = NOT_A_LIST


def test_bad_install(default_configuration):
    with pytest.raises(TypeError):
        default_configuration.install = NOT_A_LIST


def test_bad_script(default_configuration):
    with pytest.raises(TypeError):
        default_configuration.script = NOT_A_LIST
