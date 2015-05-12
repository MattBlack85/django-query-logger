from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.backends import utils

from .wrapper import CursorLoggingWrapper

QUERY_LOGGER_ON_DEBUG = getattr(settings, 'QUERY_LOGGER_ON_DEBUG', False)
DEBUG = settings.DEBUG

if QUERY_LOGGER_ON_DEBUG and not DEBUG:
    raise ImproperlyConfigured(
        "You can't set QUERY_LOGGER_ON_DEBUG to True while DEBUG is set to False")

if not DEBUG:
    # Monkeypatching django CursorWrapper with our own since there is
    # no way to use a custom one right now.
    utils.CursorWrapper = CursorLoggingWrapper
elif QUERY_LOGGER_ON_DEBUG:
    utils.CursorDebugWrapper = CursorLoggingWrapper
