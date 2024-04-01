import logging
from logging.config import dictConfig
from flask import Flask
from lib.custom_logging import (
    sample_logger_one,
    sample_logger_two,
    name_logger,
    stream_logger
)
from lib.cdp_logging import LOGGING_CONFIG, local_logger as cdp_logger

dictConfig(LOGGING_CONFIG)

# Imports the Cloud Logging client library
import google.cloud.logging

# Instantiates a client
client = google.cloud.logging.Client()

# Retrieves a Cloud Logging handler based on the environment
# you're running in and integrates the handler with the
# Python logging module. By default this captures all logs
# at INFO level and higher
client.setup_logging()

app = Flask(__name__)


@app.route("/log", methods=["GET"])
def log():
    # will not print anything since the default log level is warning
    logging.info("This is a INFO log")
    logging.error("This is a ERROR log")

    app.logger.info("[app] This is a INFO log")

    sample_logger_one.warning("Sample Logger One: WARNING")
    sample_logger_two.warning("Sample Logger Two: WARNING")

    name_logger.warning("Name Logger: WARNING")
    name_logger.propagate = False
    name_logger.warning("Name Logger: WARNING 2")
    i = [1]
    try:
        i[1] = 1
    except IndexError:
        app.logger.exception("This is a Exception log")
    return {"message": "ok"}, 200


@app.route("/stream_log", methods=["GET"])
def stream_log():
    stream_logger.debug('debug message')
    stream_logger.info('info message')
    stream_logger.warning('warn message')
    stream_logger.error('error message')
    stream_logger.critical('critical message')
    return {"message": "ok"}, 200


@app.route("/cdp_log", methods=["GET"])
def cdp_log():
    cdp_logger.debug('debug message')
    cdp_logger.info('info message')
    cdp_logger.warning('warn message')
    cdp_logger.error('error message')
    cdp_logger.critical('critical message')

    app.logger.debug('debug message')
    app.logger.info('info message')
    app.logger.warning('warn message')
    app.logger.error('error message')
    app.logger.critical('critical message')
    return {"message": "ok"}, 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8082)
