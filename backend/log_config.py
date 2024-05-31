import logging
import colorlog

log_format = (
    '%(log_color)s%(asctime)s%(reset)s - '
    '%(name)s - '
    '%(levelname_log_color)s%(levelname)s%(reset)s - '
    '%(message_log_color)s%(message)s%(reset)s'
)

log_colors = {
    'DEBUG': 'white',
    'INFO': 'white',
    'WARNING': 'white',
    'ERROR': 'white',
    'CRITICAL': 'white',
}

secondary_log_colors = {
    'levelname': {
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    },
    'message': {
        'DEBUG': 'white',
        'INFO': 'white',
        'WARNING': 'white',
        'ERROR': 'white',
        'CRITICAL': 'white',
    }
}

formatter = colorlog.ColoredFormatter(
    log_format, log_colors=log_colors, secondary_log_colors=secondary_log_colors
)

file_handler = logging.FileHandler('gas_prices.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[file_handler, stream_handler]
)

def get_logger(name):
    return logging.getLogger(name)
