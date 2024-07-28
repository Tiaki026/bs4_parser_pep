from prettytable import PrettyTable
from constants import BASE_DIR, DATETIME_FORMAT, FILE_DOWNLOAD
import datetime as dt
import csv
import logging


def file_output(results, cli_args):
    """Создание директории и файла для сохранение данных в формате csv."""
    results_dir = BASE_DIR / 'results'
    results_dir.mkdir(exist_ok=True)
    parser_mode = cli_args.mode
    now = dt.datetime.now()
    now_formatted = now.strftime(DATETIME_FORMAT)
    file_name = f'{parser_mode}_{now_formatted}.csv'
    file_path = results_dir / file_name
    with open(file_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='unix')
        writer.writerows(results)
    logging.info(f'{FILE_DOWNLOAD}{file_path}')


def control_output(results, cli_args):
    """Управление сохраняемых данных."""
    output = cli_args.output
    if output == 'pretty':
        pretty_output(results)
    elif output == 'file':
        file_output(results, cli_args)
    else:
        default_output(results)


def default_output(results):
    """Печать списка results."""
    for row in results:
        print(*row)


def pretty_output(results):
    """Печать таблицы."""
    table = PrettyTable()
    table.field_names = results[0]
    table.align = 'l'
    table.add_rows(results[1:])
    print(table)
