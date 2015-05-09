QUERY_LOGGING = {
    'formatters': {
        'wrapper_verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'wrapper_simple': {
            'format': '%(levelname)s %(message)s'
        },
        'wrapper_json': {
            '()': 'jsonlogger.JsonFormatter',
            'format': '%(levelname)s %(asctime)s %(name)s %(module)s %(lineno)d'
            '%(process)d %(thread)d %(message)s'
        },
        'wrapper_simple_json': {
            '()': 'jsonlogger.JsonFormatter',
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console_wrapper': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'wrapper_verbose',
        }
    },
    'loggers': {
        'query_logger.wrapper': {
            'handlers': ['console_wrapper'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}
