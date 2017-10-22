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

UNKNOWN = 'Unknown'


########################################################################
#
# Test Fixtures
#
########################################################################


@pytest.fixture
def empty_configuration():
    """Empty configuration object"""
    return Configuration(language=UNKNOWN, python=list(),
                         install=list(), script=list())


########################################################################
#
# Tests
#
########################################################################


# Empty tests
def test_language_empty(empty_configuration):
    assert empty_configuration.language == UNKNOWN


def test_language_empty_expect_fail(empty_configuration):
    assert empty_configuration.language == "Fail"
