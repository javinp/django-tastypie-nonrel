#!/usr/bin/env python
import os
import sys

from os.path import abspath, dirname, join
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from django.core.management import execute_manager
import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

from . import settings

if __name__ == "__main__":
    execute_manager(settings)
