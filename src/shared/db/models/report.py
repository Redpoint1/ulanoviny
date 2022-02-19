from sqlalchemy import Column, Boolean

from shared.db.models import Base
from shared.db.models.plain_text import PlainTextMixin


class Report(Base, PlainTextMixin):
    __tablename__ = 'report'
