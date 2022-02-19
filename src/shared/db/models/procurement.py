from sqlalchemy import Column, Boolean

from shared.db.models import Base
from shared.db.models.link import LinkMixin


class Procurement(Base, LinkMixin):
    __tablename__ = 'procurement'

    is_offer = Column(Boolean, nullable=False, default=False)
