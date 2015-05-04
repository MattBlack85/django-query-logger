import logging
import time

from django.db.backends.util import CursorWrapper

logger = logging.getLogger(__name__)


class CursorLoggingWrapper(CursorWrapper):

    def execute(self, sql, params=None):
        executor = self.cursor.execute
        self.db.validate_no_broken_transaction()
        with self.db.wrap_database_errors:
            if params is None:
                return self.run_sql(executor, sql)
            return self.run_sql(executor, sql, params)

    def executemany(self, sql, param_list):
        executor = self.cursor.executemany
        self.db.validate_no_broken_transaction()
        with self.db.wrap_database_errors:
            return self.run_sql(executor, sql, param_list)

    def run_sql(self, executor, sql, params=None):
        start = time.time()
        cursor = executor(sql) if not params else executor(sql, params)
        logger.info("[QUERY]: %s - params %s" % (sql, str(params)))
        logger.info("[TIME]: %s" % (end - start))
        return cursor
