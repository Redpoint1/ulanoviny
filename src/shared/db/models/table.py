from shared.db.models import Base
from shared.db.models.document import DocumentMixin


class Table(Base, DocumentMixin):
    __tablename__ = 'table'
