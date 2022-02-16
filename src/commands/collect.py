import re
import urllib3.exceptions

import bs4
import click
import requests.exceptions

from urllib.parse import urlparse, urljoin

from common.browser import Browser
from common.logger import LOGGER
from common.web import Category
from shared.db import connect_to_db, get_or_create
from shared.db.models.meeting import Meeting

URL = 'https://ulany.sk/?page={}'


@click.command()
def cli():
    return_code = 0
    engine, Session = connect_to_db()
    session = Session()

    browser = Browser()
    with browser as browser_session:
        try:
            url = URL.format(Category.MEETING.value)
            response = browser_session.get(url)
            response.raise_for_status()
            soup = bs4.BeautifulSoup(response.content, 'html.parser')

            elements = soup.select('#content-left table a')
            LOGGER.info('{} meetings have been found'.format(len(elements)))

            if len(elements) == 0:
                LOGGER.info('Done, no more meetings')
                session.close()
                return 0

            for element in reversed(elements):
                href = element['href']
                title = element.text

                model, created = get_or_create(session, Meeting, url=href, title=title)
                if not created:
                    LOGGER.info(f'Meeting "{href}" ...skipped (duplicate)')
                else:
                    LOGGER.info(f'{href} ...added')
        except requests.exceptions.HTTPError as exc:
            LOGGER.warning('Scraping {} {} ...skipping'.format(url, exc.response.status_code))
            return_code = 1

    LOGGER.info('Done')
    session.close()
    return return_code
