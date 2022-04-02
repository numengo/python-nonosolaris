from simple_settings import LazySettings
from ngoschema.config.utils import search_app_config_files

from ngoschema import settings, APP_CONTEXT, DEFAULT_CONTEXT
from nonosolaris.config import settings as local_settings

settings = LazySettings('ngoschema.config.settings',
                        'nonosolaris.config.settings',
                        *search_app_config_files('NonoSolaris', 'solaris'),
                        )

DEFAULT_CONTEXT.add_local_entries(settings=settings, **getattr(settings, 'DEFAULT_CONTEXT', {}))
APP_CONTEXT.add_local_entries(_nonosolaris_env=settings.as_dict())
