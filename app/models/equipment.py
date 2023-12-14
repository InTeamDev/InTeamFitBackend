import uuid

from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.database import Base


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    description = Column(Text)
