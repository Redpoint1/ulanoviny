from shared.db.models import Base
from shared.db.models.document import DocumentMixin


class Order(Base, DocumentMixin):
    __tablename__ = 'order'
