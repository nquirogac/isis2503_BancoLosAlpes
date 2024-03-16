from logs.db_logger import DBLogHandler

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'db': {
            'class': 'logs.db_logger.DBLogHandler',
        },
    },
    'root': {
        'handlers': ['db'],
        'level': 'INFO',
    },
}