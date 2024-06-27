from sqlalchemy import Column, Integer, String

from db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)