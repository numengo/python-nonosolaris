# -*- coding: utf-8 -*-

"""Top-level package for NonoSolaris."""

__author__ = """Cedric ROMAN"""
__email__ = 'roman@numengo.com'
__version__ = '1.1.11'

## PROTECTED REGION ID(nonosolaris.init) ENABLED START

from ngoschema.loaders import register_module
register_module('nonosolaris')

from ._settings import settings, APP_CONTEXT, DEFAULT_CONTEXT

__all__ = [
    'settings',
]
# PROTECTED REGION END
