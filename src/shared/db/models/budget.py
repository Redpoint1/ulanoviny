from shared.db.models import Base
from shared.db.models.link import LinkMixin


class Budget(Base, LinkMixin):
    __tablename__ = 'budget'
