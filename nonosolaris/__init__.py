# -*- coding: utf-8 -*-

"""Top-level package for NonoSolaris."""

__author__ = """Cedric ROMAN"""
__email__ = 'roman@numengo.com'
__version__ = '1.0.11'

from simple_settings import LazySettings
settings = LazySettings('nonosolaris.config.settings')

# PROTECTED REGION ID(nonosolaris.init) ENABLED START
from ngoschema.loaders import register_module
register_module('nonosolaris')

from .nonosolaris import *
__all__ = [
    'settings',
]
# PROTECTED REGION END
