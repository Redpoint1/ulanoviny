from urllib.parse import urlparse


class BasePlugin:
    def __init__(self):
        pass

    @staticmethod
    def url(category):
        return f'https://ulany.sk/?page={category}'

    @staticmethod
    def base_url(url, with_path=False):
        parsed = urlparse(url)
        path = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
        parsed = parsed._replace(path=path)
        parsed = parsed._replace(params='')
        parsed = parsed._replace(query='')
        parsed = parsed._replace(fragment='')
        return parsed.geturl()

    def before_request(self):
        raise NotImplementedError

    def request(self):
        raise NotImplementedError

    def after_request(self):
        raise NotImplementedError

    def parse(self, content):
        raise NotImplementedError

    def run(self):
        self.before_request()
        self.request()
        self.after_request()
