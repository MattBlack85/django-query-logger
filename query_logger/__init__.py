from django.conf import settings

if settings.DEBUG is False:
    from django.db.backends import utils
    from .wrapper import CursorLoggingWrapper

    # Monkeypatching django CursorWrapper with our own since there is
    # no way to use a custom one right now.
    utils.CursorWrapper = CursorLoggingWrapper
