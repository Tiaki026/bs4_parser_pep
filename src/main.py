import logging
import re
from collections import defaultdict
from typing import List, Tuple
from urllib.parse import urljoin

from requests_cache import CachedSession
from tqdm import tqdm

from configs import configure_argument_parser, configure_logging
from constants import (
    ARCHIVE_DOWNLOAD, ARG_COMMAND_STR, BASE_DIR,
    LATEST_VERSION, MAIN_DOC_URL, MAIN_PEP_URL,
    PARSER_DONE, PARSER_START, WHATS_NEW, PEP
)
from outputs import control_output
from utils import (
    download_link,
    get_version_details, parse_latest_versions,
    parse_pep_list, parse_whats_new, process_pep
)


def whats_new(session: CachedSession) -> List[Tuple[str, str, str]]:
    """Нововведения python."""
    whats_new_url = urljoin(MAIN_DOC_URL, 'whatsnew/')
    results = [WHATS_NEW]
    for section in tqdm(parse_whats_new(session, whats_new_url)):
        details = get_version_details(session, urljoin(whats_new_url, section))
        if details:
            results.append(details)
    return results


def latest_versions(session: CachedSession) -> List[Tuple[str, str, str]]:
    """Статусы версий python."""
    results = [LATEST_VERSION]
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
    for a_tag in parse_latest_versions(session, MAIN_DOC_URL):
        text_match = re.search(pattern, a_tag.text)
        link = a_tag['href']
        if text_match:
            version = text_match.group('version')
            status = text_match.group('status')
            results.append((link, version, status))
    return results


def download(session: CachedSession) -> None:
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


def pep(session: CachedSession) -> List[Tuple[str, int]]:
    """Парсинг сайта pep."""
    count = defaultdict(int)
    logs = []
    results = [PEP]

    for pep in tqdm(parse_pep_list(session, MAIN_PEP_URL)):
        status, log_msg = process_pep(session, pep, MAIN_PEP_URL)

        if log_msg:
            logs.append(log_msg)

        count[status] += 1

    count['Total'] = sum(count.values())
    results += list(count.items())

    return results


MODE_TO_FUNCTION = {
    'whats-new': whats_new,
    'latest-versions': latest_versions,
    'download': download,
    'pep': pep
}


def main() -> None:
    configure_logging()
    logging.info(PARSER_START)
    arg_parser = configure_argument_parser(MODE_TO_FUNCTION.keys())
    args = arg_parser.parse_args()
    logging.info(f'{ARG_COMMAND_STR}{args}')

    session = CachedSession()
    if args.clear_cache:
        session.cache.clear()

    parser_mode = args.mode
    results = MODE_TO_FUNCTION[parser_mode](session)
    if results is not None:
        control_output(results, args)
    logging.info(PARSER_DONE)


if __name__ == '__main__':
    main()
