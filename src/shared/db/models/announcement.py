from shared.db.models import Base
from shared.db.models.link import LinkMixin


class Announcement(Base, LinkMixin):
    __tablename__ = 'announcement'
