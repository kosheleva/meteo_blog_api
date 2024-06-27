from sqlalchemy import func, Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import deferred

from db import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), unique=True, nullable=False)
    email = Column(String(200), unique=True, index=True, nullable=False)
    password = deferred(Column(String, nullable=False))
    status = Column(Enum('active', 'blocked', 'deleted'), nullable=False, default='blocked')
    created_at = Column(DateTime, nullable=False, default=func.now())