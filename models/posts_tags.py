from sqlalchemy import Column, ForeignKey, Table

from db import Base


association_table = Table(
    "PostsTags",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id")),
    Column("tag_id", ForeignKey("tags.id")),
)