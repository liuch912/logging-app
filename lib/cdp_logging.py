import sys

from logging import getLogger, DEBUG, StreamHandler, Formatter, Filter, INFO


class LevelFilter(Filter):
    def __init__(self, hi=None, lo=None):
        super().__init__()
        self.hi = hi
        self.lo = lo

    def filter(self, record):
        if self.hi is None or self.lo is None:
            allow = True
        else:
            # print("Record LevelNo:", record.levelno, record.levelname)
            allow = self.hi >= record.levelno >= self.lo

        return allow


LOGGING_CONFIG = {
    "version": 1,
    "filters": {
        "info_filter": {
            "()": LevelFilter,
            "lo": 0,
            "hi": 30,
        },
        "error_filter": {
            "()": LevelFilter,
            "lo": 40,
            "hi": 50,
        },
    },
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(process)d] [%(levelname)7s] [%(module)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
        },
        "error": {
            "format": "[%(asctime)s] - [%(levelname)7s] - [%(module)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S %z",
        },
        # 'logzioFormat': {
        #     'format': '{"additional_field": "value"}',
        #     'validate': False
        # },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
            "filters": ["info_filter"],
        },
        "console-error": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
            "formatter": "error",
            "filters": ["error_filter"],
        },
        # 'logzio': {
        #     'class': 'logzio.handler.LogzioHandler',
        #     'level': 'INFO',
        #     'formatter': 'logzioFormat',
        #     'token': '<<LOG-SHIPPING-TOKEN>>',
        #     'logzio_type': 'python',
        #     'logs_drain_timeout': 5,
        #     'url': 'https://listener-wa.logz.io:8071',
        #     "add_context": True,
        # }
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "console-error"],
    },
    # 'loggers': {
    #     '': {
    #         'level': 'DEBUG',
    #         'handlers': ['logzio'],
    #         'propagate': True
    #     }
    # }
}


def _setup_local_logger():
    logger = getLogger()
    logger.handlers.clear()
    logger.setLevel(INFO)

    handler = StreamHandler(sys.stdout)
    formatter = Formatter(
        fmt="[%(asctime)s] [%(process)d] [%(levelname)7s] [%(module)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %z",
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


local_logger = getLogger()
# local_logger = _setup_local_logger()

