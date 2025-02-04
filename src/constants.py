from pathlib import Path

MAIN_DOC_URL = 'https://docs.python.org/3/'
BASE_DIR = Path(__file__).parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
MAIN_PEP_URL = 'https://peps.python.org/'

EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred'),
    'F': ('Final'),
    'P': ('Provisional'),
    'R': ('Rejected'),
    'S': ('Superseded'),
    'W': ('Withdrawn'),
    '': ('Draft', 'Active'),
}
UNEXPECTED_STATUS = (
    '\n ❗️Статус не совпадает❗️:  {link}'
    '\n \n      Полученный статус: {status}'
    '\n      Ожидаемый статус: {expected}'
    '\n'
)

WHATS_NEW = ('Ссылка на статью', 'Заголовок', 'Редактор, автор')
LATEST_VERSION = ('Ссылка на документацию', 'Версия', 'Статус')
PEP = ('Статус', 'Количество')

PARSER_DONE = '✅ Парсер завершил работу.'
PARSER_START = '▶️ Парсер запущен!'
ARCHIVE_DOWNLOAD = '💾 Архив был загружен и сохранён: '
FILE_DOWNLOAD = '💾 Файл с результатами был сохранён: '
WRONG_TAG = '❌ Не найден тег '
NO_CONTENT = '❌ Ничего не нашлось'
ERROR_DOWNLOAD_PAGE = '❌ Возникла ошибка при загрузке страницы '

HELP_PARSER = 'Парсер документации Python'
PARSER_MODE = 'Режимы работы парсера'
CLEAR_CACHE = 'Очистка кеша'
ADD_DATA_OUTPUT = 'Дополнительные способы вывода данных'
ARG_COMMAND_STR = 'Аргументы командной строки: '
