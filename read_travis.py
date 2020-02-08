#!/usr/bin/env python
# -*- coding: utf-8 -*-
########################################################################
#
# read_travis.py - Dummy module to read Travis configuration
#
########################################################################


########################################################################
#
# Imports
#
########################################################################

from __future__ import print_function
import os
import argparse
import logging
# Set logging level
logging.basicConfig(format='%(asctime)s [%(levelname)s]\t: %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Non-standard modules
try:
    import yaml
except ImportError:
    logger.error("This code requires the yaml module, which does not seem " +
                 "to be installed. You can install it with " +
                 "\"pip install PyYAML\"")
    exit()

########################################################################
#
# Defines
#
########################################################################

TRAVIS_FILENAME = ".travis.yml"

########################################################################
#
# Helpers / Functions
#
########################################################################


########################################################################
#
# Classes
#
########################################################################

########################################################################
# Configuration
########################################################################


class Configuration(object):

    @classmethod
    def import_cfg(cls, folder=os.getcwd(), filename=TRAVIS_FILENAME):
        """
        Read in the configuration

        Args:
            folder (str): Folder containing the configuration.
            filename (str): Configuration filename.

        Returns:
            Configuration object
        """

        configFilename = os.path.join(folder, filename)

        try:
            with open(configFilename) as f:
                configData = yaml.load(f, Loader=yaml.FullLoader)
        except IOError as e:
            print("An issue occurred accessing {0} ({1})".format(configFilename,
                                                                 e.strerror))
            return cls(language="Unknown", python=list(),
                       install=list(), script=list())

        language = configData.get('language', 'Unknown')
        python = configData.get('python', list())
        install = configData.get('install', list())
        script = configData.get('script', list())

        return cls(language, python, install, script)

    def __init__(self, language, python, install, script):
        """
        Travis configuration
        """
        self.language = language
        self.python = python
        self.install = install
        self.script = script

    def __repr__(self):
        return 'Configuration({!r}, {!r}, {!r}, {!r})'.format(self.language,
                                                              self.python,
                                                              self.install,
                                                              self.script)

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, l):
        if not isinstance(l, str):
            raise TypeError("language must be set to a string")
        self._language = l

    @property
    def python(self):
        return self._python

    @python.setter
    def python(self, p):
        if not isinstance(p, list):
            raise TypeError("python must be set to a list")
        self._python = p

    @property
    def install(self):
        return self._install

    @install.setter
    def install(self, i):
        if not isinstance(i, list):
            raise TypeError("install must be set to a list")
        self._install = i

    @property
    def script(self):
        return self._script

    @script.setter
    def script(self, s):
        if not isinstance(s, list):
            raise TypeError("script must be set to a list")
        self._script = s


########################################################################
#
# Main
#
########################################################################


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--root_folder",
                        # Default root path
                        default=os.path.dirname(os.path.realpath(__file__)),
                        help="Root folder")
    args = parser.parse_args()

    config = Configuration.import_cfg(folder=args.root_folder)
