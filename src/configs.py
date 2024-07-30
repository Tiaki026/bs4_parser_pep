import argparse
import logging
from logging.handlers import RotatingFileHandler

from constants import (
    ADD_DATA_OUTPUT, BASE_DIR, CLEAR_CACHE,
    HELP_PARSER, PARSER_MODE
)

LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'


def configure_argument_parser(available_modes):
    """Конфиг парсера c очисткой кеша."""
    parser = argparse.ArgumentParser(description=HELP_PARSER)
    parser.add_argument(
        'mode',
        choices=available_modes,
        help=PARSER_MODE
    )
    parser.add_argument(
        '-c',
        '--clear-cache',
        action='store_true',
        help=CLEAR_CACHE
    )
    parser.add_argument(
        '-o',
        '--output',
        choices=('pretty', 'file'),
        help=ADD_DATA_OUTPUT
    )
    return parser


def configure_logging():
    """Конфиг логов.
    Сохранение в директорию logs,
    максимальный объем файла 6мб,
    максимальное количество файлов -5.
    """
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'parser.log'
    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10 ** 6, backupCount=5, encoding='utf-8'
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )
