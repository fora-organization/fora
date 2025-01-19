from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List

from .base import Base


"""
    1. Admin
    2. User
    3. Seller
"""


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    users: Mapped[List[int]] = relationship(back_populates='role')