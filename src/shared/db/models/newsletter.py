from shared.db.models import Base
from shared.db.models.link import LinkMixin


class Newsletter(Base, LinkMixin):
    __tablename__ = 'newsletter'
