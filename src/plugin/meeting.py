import bs4
import requests.exceptions

from plugin import BasePlugin
from common.browser import Browser
from common.web import Category
from common.logger import LOGGER
from common.database import Database
from shared.db.models.meeting import Meeting


class MeetingPlugin(BasePlugin):
    def __init__(self):
        super().__init__()

    def before_request(self):
        LOGGER.info('Start scrapping meetings')

    def request(self):
        try:
            with Database() as session:
                with Browser() as browser_session:
                    url = self.url(Category.MEETING.value)
                    response = browser_session.get(url)
                    response.raise_for_status()
                    soup = bs4.BeautifulSoup(response.content, 'html.parser')

                    elements = soup.select('#content-left table a')
                    LOGGER.info('{} meetings have been found'.format(len(elements)))

                    if len(elements) == 0:
                        LOGGER.info('Done, no more meetings')
                        return

                    for element in reversed(elements):
                        href = element['href']
                        title = element.text

                        model, created = session.get_or_create(Meeting, url=href, title=title)
                        if not created:
                            LOGGER.info(f'Meeting "{href}" ...skipped (duplicate)')
                        else:
                            LOGGER.info(f'{href} ...added')
        except requests.exceptions.HTTPError as exc:
            LOGGER.warning('Scraping {} {} ...skipping'.format(url, exc.response.status_code))
            raise exc

    def after_request(self):
        LOGGER.info('Finished scrapping meetings')
