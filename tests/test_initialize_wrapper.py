from django.test import TestCase
from query_logger.wrapper import CursorLoggingWrapper


class InitializeWrapperTestCase(TestCase):

    def test_debug_off_wrapper_on(self):
        """
        Tests are run by default with DEBUG = False
        so assert the monkeypatching has worked.
        """
        from django.db.backends import utils
        self.assertEqual(utils.CursorWrapper, CursorLoggingWrapper)
