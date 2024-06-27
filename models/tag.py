from sqlalchemy import Column, Integer, String

from db import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, unique=True)