# import hashlib

from sqlalchemy import Column, String, Integer, DateTime, text, UniqueConstraint
# from sqlalchemy.ext.hybrid import hybrid_property


class PlainTextMixin:
    __table_args__ = (UniqueConstraint('date', 'title', name='_report_title'),)

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    title = Column(String, nullable=False)
    # hash = Column(String, nullable=False, unique=True)
    added = Column(DateTime, nullable=False, server_default=text("(DATETIME('now'))"))
    weekly = Column(DateTime)
    monthly = Column(DateTime)

    # smaller DB size
    # @hybrid_property
    # def title(self):
    #     return self._title
    #
    # @title.setter
    # def title(self, value):
    #     self._title = value
    #     hashable = f'{self._date}-{self._title}'
    #     self.hash = hashlib.sha256(bytes(hashable, 'utf8')).hexdigest()
    #
    # @hybrid_property
    # def date(self):
    #     return self._date
    #
    # @date.setter
    # def date(self, value):
    #     self._date = value
    #     hashable = f'{self._date}-{self._title}'
    #     self.hash = hashlib.sha256(bytes(hashable, 'utf8')).hexdigest()
