import datetime
import re
from urllib.parse import urljoin

import bs4
import requests.exceptions

from plugin import BasePlugin
from common.browser import Browser
from common.web import Category
from common.logger import LOGGER
from common.database import Database
from shared.db.models.resolution import Resolution


class ResolutionPlugin(BasePlugin):
    def __init__(self):
        super().__init__()

    def before_request(self):
        LOGGER.info('Start scrapping resolutions')

    def request(self):
        with Database() as session:
            with Browser() as browser_session:
                url = self.url(Category.RESOLUTION.value)
                loop = True
                while loop:
                    try:
                        response = browser_session.get(url)
                        response.raise_for_status()
                        soup = bs4.BeautifulSoup(response.content, 'html.parser')

                        elements = soup.select('#dokumenty table.tabulka tr:not(.hlavicka)')

                        if len(elements) == 0:
                            LOGGER.info('Done, no more resolutions')
                            return

                        for element in elements:
                            published, _, _, title, _, document = element.findChildren('td')
                            link = document.findChild('a').attrs.get('href')
                            size_in_mb = re.search(r'([0-9\.]+)', document.text).groups()[0]
                            is_pdf = re.search(r'\.pdf$', link)
                            if is_pdf:
                                model, created = session.get_or_create(
                                    Resolution,
                                    published=datetime.date.fromisoformat(published.text),
                                    title=title.text,
                                    url=link,
                                    size_in_mb=size_in_mb
                                )
                                if not created:
                                    LOGGER.info(f'Resolution {model.url} ...skipped (duplicate)')
                                    loop = False
                                else:
                                    LOGGER.info(f'{model.url} ...added')
                            else:
                                LOGGER.warning(f'Resolution {model.url} ...skipped (not PDF)')
                        next_url = soup.select_one(
                            '#dokumenty table:first-of-type [align="right"] a:nth-last-child(2)'
                        ).attrs.get('href')
                        next_url = urljoin(self.base_url(response.url), next_url)

                        # FIXME: first page can be w/o the page number
                        if next_url == url:
                            return
                        url = next_url
                    except requests.exceptions.HTTPError as exc:
                        LOGGER.warning('Scraping {} {} ...skipping'.format(url, exc.response.status_code))
                        raise exc

    def after_request(self):
        LOGGER.info('Finished scrapping resolutions')
