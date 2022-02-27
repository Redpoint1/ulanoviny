from shared.db.models import Base
from shared.db.models.document import DocumentMixin


class Transcript(Base, DocumentMixin):
    __tablename__ = 'transcript'
