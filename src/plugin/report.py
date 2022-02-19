import re

import bs4
import requests.exceptions

from plugin import BasePlugin
from common.browser import Browser
from common.web import Category
from common.logger import LOGGER
from common.database import Database
from shared.db.models.report import Report


class ReportPlugin(BasePlugin):
    def __init__(self):
        super().__init__()

    def before_request(self):
        LOGGER.info('Start scrapping reports')

    def request(self):
        try:
            with Database() as session:
                with Browser() as browser_session:
                    url = self.url(Category.REPORT.value)
                    response = browser_session.get(url)
                    response.raise_for_status()
                    soup = bs4.BeautifulSoup(response.content, 'html.parser')

                    elements = soup.select('#content-left tr')
                    LOGGER.info('{} reports have been found'.format(len(elements)))

                    if len(elements) == 0:
                        LOGGER.info('Done, no more reports')
                        return

                    for element in elements:
                        date, title = element.findChildren('td')

                        title = re.sub(r'[\n\s]+', ' ', title.text)

                        model, created = session.get_or_create(Report, date=date.text.strip(), title=title.strip())
                        if not created:
                            LOGGER.info(f'Report "{model.title[:30]}..." ...skipped (duplicate)')
                        else:
                            LOGGER.info(f'"{model.title[:40]}..." ...added')
        except requests.exceptions.HTTPError as exc:
            LOGGER.warning('Scraping {} {} ...skipping'.format(url, exc.response.status_code))
            raise exc

    def after_request(self):
        LOGGER.info('Finished scrapping reports')
