class BasePlugin:
    def __init__(self):
        pass

    @staticmethod
    def url(category):
        return f'https://ulany.sk/?page={category}'

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
