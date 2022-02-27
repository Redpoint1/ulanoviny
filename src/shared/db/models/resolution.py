from shared.db.models import Base
from shared.db.models.document import DocumentMixin


class Resolution(Base, DocumentMixin):
    __tablename__ = 'resolution'
