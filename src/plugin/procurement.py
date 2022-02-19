import re

import bs4
import requests.exceptions

from plugin import BasePlugin
from common.browser import Browser
from common.web import Category
from common.logger import LOGGER
from common.database import Database
from shared.db.models.procurement import Procurement


class ProcurementPlugin(BasePlugin):
    def __init__(self):
        super().__init__()

    def before_request(self):
        LOGGER.info('Start scrapping procurement')

    def request(self):
        try:
            with Database() as session:
                with Browser() as browser_session:
                    url = self.url(Category.PROCUREMENT.value)
                    response = browser_session.get(url)
                    response.raise_for_status()
                    soup = bs4.BeautifulSoup(response.content, 'html.parser')

                    main_element = soup.select_one('#content-left ol')
                    procurements = main_element.select('a')
                    offers = main_element.find_next_siblings('a')
                    LOGGER.info('{} procurements have been found'.format(len(procurements)))

                    if len(procurements) == 0:
                        LOGGER.info('Done, no more procurements')

                    for element in procurements:
                        href = element['href']
                        title = element.text

                        model, created = session.get_or_create(Procurement, url=href, title=title)
                        if not created:
                            LOGGER.info(f'Procurement "{href}" ...skipped (duplicate)')
                        else:
                            LOGGER.info(f'{href} ...added')

                    LOGGER.info('{} offers have been found'.format(len(offers)))

                    if len(offers) == 0:
                        LOGGER.info('Done, no more offers')
                        return

                    for element in offers:
                        href = element['href']
                        title = element.text

                        model, created = session.get_or_create(Procurement, url=href, title=title, is_offer=True)
                        if not created:
                            LOGGER.info(f'Offer "{href}" ...skipped (duplicate)')
                        else:
                            LOGGER.info(f'{href} ...added')
        except requests.exceptions.HTTPError as exc:
            LOGGER.warning('Scraping {} {} ...skipping'.format(url, exc.response.status_code))
            raise exc

    def after_request(self):
        LOGGER.info('Finished scrapping procurements')
