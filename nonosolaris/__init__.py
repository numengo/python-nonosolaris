# -*- coding: utf-8 -*-

"""Top-level package for NonoSolaris."""

__author__ = """Cedric ROMAN"""
__email__ = 'roman@numengo.com'
__version__ = '1.1.2'

from simple_settings import LazySettings
from ngoschema.config.utils import search_app_config_files

settings = LazySettings('nonosolaris.config.settings', *search_app_config_files('NonoSolaris', 'solaris'))

# PROTECTED REGION ID(nonosolaris.init) ENABLED START
from ngoschema.loaders import register_module
register_module('nonosolaris')

from ngoschema import DEFAULT_CONTEXT, APP_CONTEXT
DEFAULT_CONTEXT.add_local_entries(**getattr(settings, 'DEFAULT_CONTEXT', {}))
# in init, settings are available in app context whereas it is in default context in cli
APP_CONTEXT.add_local_entries(settings=settings, _nonosolaris_env=settings.as_dict())

from ._nonosolaris import *

__all__ = [
    'settings',
]
# PROTECTED REGION END
