from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import Optional, List

from .base import Base
from .role import Role
from .associates import user_cart_assoc_table, user_favorites_assoc_table
from .product import Product

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[Optional[str]] = mapped_column(String(50))
    first_name: Mapped[Optional[str]] = mapped_column(String(50))
    last_name: Mapped[Optional[str]] = mapped_column(String(50))
    phone_number: Mapped[Optional[str]] = mapped_column(String(15))
    zip_code: Mapped[Optional[str]] = mapped_column(String(50))
    role_id: Mapped[Optional[int]] = ForeignKey('role.id', ondelete='CASCADE')

    role: Mapped[Optional[Role]] = relationship(back_populates="user")
    cart: Mapped[List[Product]] = relationship(secondary=user_cart_assoc_table, back_populates="cart_users")
    favorites: Mapped[List[Product]] = relationship(secondary=user_favorites_assoc_table, back_populates="fav_users")