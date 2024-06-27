from sqlalchemy import func, Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, backref

from db import Base
from .posts_tags import association_table


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    content = Column(String, nullable=False)
    is_visible = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())

    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    author = relationship("Author", backref=backref("author", lazy="dynamic"))
    category = relationship("Category")

    tags = relationship('Tag', secondary=association_table)