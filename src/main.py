import re
from urllib.parse import urljoin

import requests_cache
from tqdm import tqdm

from constants import (
    MAIN_DOC_URL, BASE_DIR, EXPECTED_STATUS, WHATS_NEW,
    LATEST_VERSION, PARSER_DONE, PARSER_START, ARCHIVE_DOWNLOAD, PEP
)
from configs import configure_argument_parser, configure_logging
from outputs import control_output
from utils import (
    parse_whats_new, get_version_details,
    parse_latest_versions, download_link
)
import logging


def whats_new(session):
    """Нововведения python."""
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    results = [WHATS_NEW]
    for section in tqdm(parse_whats_new(session, whats_new_url)):
        version_a_tag = section.find('a')
        version_link = urljoin(whats_new_url, version_a_tag['href'])
        details = get_version_details(session, version_link)
        if details:
            results.append(details)
    return results


def latest_versions(session):
    """Статусы версий python."""
    results = [LATEST_VERSION]
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
    for a_tag in parse_latest_versions(session, MAIN_DOC_URL):
        text = a_tag.text
        text_match = re.search(pattern, text)
        link = a_tag['href']
        if text_match:
            version = text_match.group('version')
            status = text_match.group('status')
            results.append((link, version, status))
    return results


def download(session):
    """Скачивание файла."""
    downloads_url = urljoin(MAIN_DOC_URL, 'download.html')
    filename = download_link(session, downloads_url).split('/')[-1]
    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename
    with open(archive_path, 'wb') as file:
        file.write(
            session.get(download_link(session, downloads_url)).content
        )
    logging.info(f'{ARCHIVE_DOWNLOAD}{archive_path}')


def pep(session):
    """Парсинг сайта pep."""

    results = [PEP]

    return results


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep
}


def main():
    configure_logging()
    logging.info(PARSER_START)
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'Аргументы командной строки: {args}')

    session = requests_cache.CachedSession()
    if args.clear_cache:
        session.cache.clear()

    parser_mode = args.mode
    results = MODE_TO_FUNCTION[parser_mode](session)
    if results is not None:
        control_output(results, args)
    logging.info(PARSER_DONE)


if __name__ == '__main__':
    main()
