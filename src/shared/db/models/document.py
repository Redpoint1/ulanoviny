from sqlalchemy import Column, String, Integer, DateTime, Date, text, DECIMAL


class DocumentMixin:
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False)
    published = Column(Date, nullable=False)
    added = Column(DateTime, nullable=False, server_default=text("(DATETIME('now'))"))
    size_in_mb = Column(DECIMAL(10, 2))
    weekly = Column(DateTime)
    monthly = Column(DateTime)
