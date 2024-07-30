import logging
import re
from typing import Optional, Tuple
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag
from bs4.element import ResultSet
from requests import RequestException, Response
from requests_cache import CachedSession

from constants import ERROR_DOWNLOAD_PAGE, NO_CONTENT, WRONG_TAG
from exceptions import ParserFindTagException
from tqdm import tqdm


def get_response(session: CachedSession, url: str) -> (Response | Exception):
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


def find_tag(soup: BeautifulSoup, tag: str, attrs=None) -> (Tag | Exception):
    """Перехват ошибки поиска тегов."""
    searched_tag = soup.find(tag, attrs=(attrs or {}))
    if searched_tag is None:
        error_msg = f'{WRONG_TAG}{tag} {attrs}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag


def get_soup(session: CachedSession, url: str) -> (BeautifulSoup | None):
    """Получение супа."""
    response = get_response(session, url)
    if response is None:
        return
    return BeautifulSoup(response.text, features='lxml')


def parse_whats_new(session: CachedSession, url: str):
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


def parse_latest_versions(
    session: CachedSession, url: str
) -> (ResultSet | None):
    """Парсинг статусов версий Python."""
    sidebar = find_tag(
        get_soup(session, url),
        'div', {'class': 'sphinxsidebarwrapper'}
    )
    ul_tags = sidebar.find_all('ul')
    for ul in ul_tags:
        if 'All versions' in ul.text:
            return ul.find_all('a')
        raise Exception(NO_CONTENT)
    return [a_tag.text for a_tag in ul.find_all('a')]


def download_link(session: CachedSession, url: str) -> str:
    table_tag = find_tag(
        get_soup(session, url),
        'table', attrs={'class': 'docutils'}
    )
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    return urljoin(url, pdf_a4_tag['href'])


def parse_pep(session: CachedSession, url: str):
    tag = find_tag(
        get_soup(session, url),
        'section', {'id': 'numerical-index'}
    )
    peps = find_tag(tag, 'tbody').find_all('tr')
    if not peps:
        raise ParserFindTagException(NO_CONTENT)
    return [pep for pep in tqdm(peps)]
