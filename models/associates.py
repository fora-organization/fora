from sqlalchemy import Table, Column, Integer, ForeignKey

from .base import Base


user_cart_assoc_table = Table(
    'user_cart',
    Base.metadata,
    Column("user_id", Integer, ForeignKey('user.id'), primary_key=True),
    Column("product_id", Integer, ForeignKey("product.id"), primary_key=True),
    Column("quantity", Integer, default=1)
)


user_favorites_assoc_table = Table(
    "user_favorites",
    Base.metadata,
Column("user_id", Integer, ForeignKey('user.id'), primary_key=True),
    Column("product_id", Integer, ForeignKey("product.id"), primary_key=True)
)