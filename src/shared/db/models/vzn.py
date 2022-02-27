from shared.db.models import Base
from shared.db.models.document import DocumentMixin


class VZN(Base, DocumentMixin):
    __tablename__ = 'vzn'
