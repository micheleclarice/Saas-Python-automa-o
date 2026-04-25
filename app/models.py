from app.sqlalchemy import Column, String, Text
from app.pgvector.sqlalchemy import Vector
from app..database import Base
import uuid


def gen():
    return str(uuid.uuid4())


class Document(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, default=gen)
    company_id = Column(String)
    content = Column(Text)
    embedding = Column(Vector(1536))