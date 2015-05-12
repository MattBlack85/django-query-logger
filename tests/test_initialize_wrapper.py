import importlib
import sys

from django.core.exceptions import ImproperlyConfigured
from django.db.backends.utils import CursorDebugWrapper
from django.test import TestCase
from query_logger.wrapper import CursorLoggingWrapper


class InitializeWrapperTestCase(TestCase):

    def test_debug_false_wrapper_active(self):
        """
        Tests are run by default with DEBUG = False
        so assert the monkeypatching has worked.
        """
        from django.db.backends import utils
        self.assertEqual(utils.CursorWrapper, CursorLoggingWrapper)

    def test_debug_false_query_logger_on_debug_true(self):
        with self.settings(DEBUG=False,
                           QUERY_LOGGER_ON_DEBUG=True):
            with self.assertRaises(ImproperlyConfigured):
                importlib.reload(sys.modules['query_logger'])

    def test_debug_true_query_logger_on_debug_false(self):
        with self.settings(DEBUG=True):
            from django.conf import settings
            print(settings.__dict__)
            importlib.reload(sys.modules['query_logger'])
            from django.db.backends import utils
            self.assertEqual(utils.CursorDebugWrapper, CursorDebugWrapper)

    def test_debug_true_query_logger_on_debug_true(self):
        with self.settings(DEBUG=True,
                           QUERY_LOGGER_ON_DEBUG=True):
            importlib.reload(sys.modules['query_logger'])
            from django.db.backends import utils
            self.assertEqual(utils.CursorDebugWrapper, CursorLoggingWrapper)
            # Setting back the CursorDebugWrapper since we're playing with global settings which are
            # not reset between tests
            utils.CursorDebugWrapper = CursorDebugWrapper
