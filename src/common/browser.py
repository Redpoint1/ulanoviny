from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from common.logger import LOGGER


class BaseBrowser:
    def __init__(self):
        pass

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, *args):
        raise NotImplementedError


class Browser(BaseBrowser):
    def __init__(self, max_retries: int = 5):
        LOGGER.info("Creating browser session")
        self.session = Session()

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

    def __enter__(self):
        return self.session.__enter__()

    def __exit__(self, *args):
        self.session.__exit__(*args)

    def __getattr__(self, item):
        return self.session.__getattribute__(item)
