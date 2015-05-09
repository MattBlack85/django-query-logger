#! /usr/bin/env python

import os
import sys


def run_tests():
    import django
    from django.conf import settings
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            },
        },
    )

    sys.path.append(os.path.abspath(__file__))

    if hasattr(django, 'setup'):
        django.setup()

    from django_nose import NoseTestSuiteRunner

    test_runner = NoseTestSuiteRunner(verbosity=1)
    return test_runner.run_tests([
        'tests',
    ])


def main():
    failures = run_tests()
    sys.exit(failures)

if __name__ == '__main__':
    main()
