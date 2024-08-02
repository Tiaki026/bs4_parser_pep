import logging
import re
from typing import List, Optional, Tuple, Union
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag
from requests import RequestException, Response
from requests_cache import CachedSession

from constants import (
    ERROR_DOWNLOAD_PAGE, EXPECTED_STATUS,
    NO_CONTENT, UNEXPECTED_STATUS, WRONG_TAG
)
from exceptions import ParserFindTagException


def get_response(
    session: CachedSession, url: str
) -> Union[Response, Exception]:
    """Перехват ошибки RequestException."""
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'{ERROR_DOWNLOAD_PAGE}{url}',
            stack_info=True
        )


def find_tag(
    soup: BeautifulSoup, tag: str, attrs=None
) -> Union[Tag, Exception]:
    """Перехват ошибки поиска тегов."""
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'{WRONG_TAG}{tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def get_soup(session: CachedSession, url: str) -> Union[BeautifulSoup, None]:
    """Получение супа."""
    response = get_response(session, url)
    if response is None:
        return
    return BeautifulSoup(response.text, features='lxml')


def parse_whats_new(session: CachedSession, url: str) -> List[str]:
    """Парсинг новостей Python."""
    main_div = find_tag(
        get_soup(session, url),
        'section', attrs={'id': 'what-s-new-in-python'}
    )
    div_with_ul = find_tag(main_div, 'div', attrs={'class': 'toctree-wrapper'})
    section_by_python = div_with_ul.find_all(
        'li', attrs={'class': 'toctree-l1'}
    )
    return [section.find('a')['href'] for section in section_by_python]


def get_version_details(
    session: CachedSession, url: str
) -> Optional[Tuple[str, str, str]]:
    """Получение деталей версии."""
    h1 = (find_tag(get_soup(session, url), 'h1')).text
    dl = (find_tag(get_soup(session, url), 'dl')).text
    dl_text = dl.replace('\n', ' ')
    return url, h1, dl_text


def parse_latest_versions(session: CachedSession, url: str) -> List[str]:
    """Парсинг статусов версий Python."""
    sidebar = find_tag(
        get_soup(session, url),
        'div', {'class': 'sphinxsidebarwrapper'}
    )
    ul_tags = sidebar.find_all('ul')
    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all('a')
            break
    else:
        raise ParserFindTagException(NO_CONTENT)
    return a_tags


def download_link(session: CachedSession, url: str) -> str:
    """Получение ссылки для скачивания."""
    table_tag = find_tag(
        get_soup(session, url),
        'table', attrs={'class': 'docutils'}
    )
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    return urljoin(url, pdf_a4_tag['href'])


def parse_pep_list(session: CachedSession, url: str) -> List[Tag]:
    """Парсинг peps."""
    tag = find_tag(
        get_soup(session, url),
        'section',
        {'id': 'numerical-index'}
    )
    peps = find_tag(tag, 'tbody').find_all('tr')
    if not peps:
        raise ParserFindTagException(NO_CONTENT)

    return peps


def process_pep(
    session: CachedSession, pep: Tag, url: str
) -> Union[Tuple[str, str], str]:
    """Процесс парсинга pep."""
    status = find_tag(pep, 'abbr').text[1:]
    expected = EXPECTED_STATUS.get(status, [])

    link = urljoin(url, find_tag(pep, 'a')['href'] + '/')
    status = find_tag(get_soup(session, link), 'abbr').text

    if status not in expected:
        log_msg = UNEXPECTED_STATUS.format(
            link=link,
            status=status,
            expected=expected
        )
        return status, log_msg
    return status
