from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Float, Integer
from typing import Optional, List

from .base import Base
from .associates import user_cart_assoc_table, user_favorites_assoc_table


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500))
    price: Mapped[float] = mapped_column(Float)
    quantity: Mapped[int] = mapped_column(Integer)
    image_url: Mapped[str] = mapped_column(String(255))
    rating: Mapped[float] = mapped_column(Float)

    cart_users: Mapped[List["User"]] = relationship(secondary=user_cart_assoc_table, back_populates="cart")
    fav_users: Mapped[List["User"]] = relationship(secondary=user_favorites_assoc_table, back_populates="favorites")
    review: Mapped[List['Review']] = relationship(back_populates='product')

    def __repr__(self):
        return (
            f"id:{self.id}, name:'{self.name}', description:'{self.description}', "
            f"price:{self.price}, quantity:{self.quantity}, image_url:'{self.image_url}', "
            f"rating:{self.rating}"
        )
