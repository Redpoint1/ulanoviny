from shared.db import connect_to_db, get_or_create


class Database:
    def __init__(self, database="ulanoviny"):
        self.database = database
        self.engine = None
        self.session = None

    def open(self):
        engine, Session = connect_to_db(self.database)
        self.engine = engine
        self.session = Session()
        return self

    def close(self):
        self.session.close()

    def get_or_create(self, model, **kwargs):
        return get_or_create(self.session, model, **kwargs)

    def __enter__(self):
        return self.open()

    def __exit__(self, *args):
        self.close()

    def __getattr__(self, *args, **kwargs):
        return self.session.__getattribute__(*args, **kwargs)
