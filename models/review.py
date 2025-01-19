from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import Optional

from .base import Base
from .product import Product


class Review(Base):
    __tablename__ = 'review'
    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[float] = mapped_column()
    text: Mapped[Optional[str]] = mapped_column(String(500))
    user_image_url: Mapped[Optional[str]] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))

    product: Mapped[Product] = relationship(back_populates='review')