from shared.db.models import Base
from shared.db.models.document import DocumentMixin


class Contract(Base, DocumentMixin):
    __tablename__ = 'contract'
