import os
# import random
# import re
#
# import bs4
#
# from datetime import datetime
# from typing import Union

from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# from common.exceptions import NoProxyException, UnathorizedException
from common.logger import LOGGER
# from shared.db.models.proxy import Proxy
# from shared.db import connect_to_db, get_or_create


SECRET_ID = os.getenv("SECRET_ID")

PROXIES = {
    # "socks4://5.102.58.41:5678",  # ok
    # "socks4://77.48.137.3:50523",  # ok
    # "socks4://82.142.87.2:4145",  # cloudflare
    # "socks4://88.146.196.181:4153",  # timeout
    # "socks4://90.183.158.50:44964",  # cloudflare
    # "socks4://93.91.146.30:34350",  # cloudflare
    # "socks4://93.99.13.46:4153",  # cloudflare
    # "socks4://178.20.137.178:37712",  # timeout
    # "socks4://185.176.136.141:4153",  # cloudflare
    # "socks4://188.75.186.152:4145",  # timeout
    # "socks4://109.238.222.5:42401",  # cloudflare
    # "socks4://193.85.228.182:47747",  # ok
    # "socks4://194.213.43.166:59316",  # cloudflare
    # "socks4://194.228.84.10:4145",  # cloudflare
    # "socks4://194.228.129.189:56211",  # cloudflare
    # "socks4://213.192.25.241:42489",  # timeout
    # "socks4://217.145.199.45:56746",  # cloudflare
}


# def get_random_proxy(proxies: Union[list, set]):
#     engine, db_session = connect_to_db()
#     session = db_session()
#
#     today = datetime.utcnow().date()
#     instance = session.query(Proxy).filter_by(used_in=today, failed=False).first()
#     if instance is None:
#         instances = session.query(Proxy).filter_by(used_in=today, failed=True).all()
#         possible_proxies = list(proxies - {proxy.proxy for proxy in instances})
#         if len(possible_proxies) == 0:
#             raise NoProxyException('No proxy available')
#
#         instance = Proxy(proxy=random.choice(possible_proxies))
#         session.add(instance)
#         session.commit()
#
#     result = {"http": instance.proxy, "https": instance.proxy}
#     session.close()
#
#     return result


# CHOOSED_PROXY = get_random_proxy(PROXIES)
CHOOSED_PROXY = {}


class BaseBrowser:
    def __init__(self):
        pass

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, *args):
        raise NotImplementedError

    def get_random_proxy(self, proxies: list):
        raise NotImplementedError


class Browser(BaseBrowser):
    def __init__(self, max_retries: int = 5):
        LOGGER.info("Creating browser session")
        self.session = Session()

        self.session.proxies = CHOOSED_PROXY
        LOGGER.info("Using %s as a proxy", self.session.proxies.get('http'))

        LOGGER.info("Injecting headers into the browser")
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/88.0",
            "Accept-Language": "sk,en-US;q=0.7,en;q=0.3",
        })

        if max_retries:
            retry_strategy = Retry(
                total=max_retries
            )

            adapter = HTTPAdapter(max_retries=retry_strategy)
            self.session.mount("https://", adapter)
            self.session.mount("http://", adapter)

        super().__init__()
    #
    # def check_cloudflare(self, session, response):
    #     soup = bs4.BeautifulSoup(response.content, 'html.parser')
    #     if response.status_code == 403 and 'Cloudflare' in soup.title.text:
    #         instance, _ = get_or_create(session, Proxy, proxy=self.session.proxies.get('http'))
    #         instance.failed = True
    #         session.commit()
    #         return True
    #     return False
    #
    # def disable_proxy(self, session):
    #     instance, _ = get_or_create(session, Proxy, proxy=self.session.proxies.get('http'))
    #     instance.failed = True
    #     LOGGER.info('Disabling proxy %s', instance.proxy)
    #     session.commit()
    #     LOGGER.info('Commited')

    def __enter__(self):
        return self.session.__enter__()

    def __exit__(self, *args):
        self.session.__exit__(*args)

    def __getattr__(self, item):
        return self.session.__getattribute__(item)
