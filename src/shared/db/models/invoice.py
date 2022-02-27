from shared.db.models import Base
from shared.db.models.document import DocumentMixin


class Invoice(Base, DocumentMixin):
    __tablename__ = 'invoice'
