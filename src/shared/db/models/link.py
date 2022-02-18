from sqlalchemy import Column, String, Integer, DateTime, text


class LinkMixin:
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False)
    added = Column(DateTime, nullable=False, server_default=text("(DATETIME('now'))"))
    weekly = Column(DateTime)
    monthly = Column(DateTime)
