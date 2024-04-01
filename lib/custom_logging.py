import logging

sample_logger_one = logging.getLogger('sample_one')
sample_logger_two = logging.getLogger('sample_two')

name_logger = logging.getLogger(__name__)

# create logger
stream_logger = logging.getLogger('simple_example')
stream_logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
stream_logger.addHandler(ch)

