from .base import Base, Session, create_db, drop_db
from .role import Role
from .user import User
from .review import Review
from .product import Product
from .associates import user_cart_assoc_table
from .product import user_favorites_assoc_table

create_db()

"""
    1. Користувач
    2. Роль Адмін/покупець/продукт
    3. Продукт
    4. Кошик
    5. Улюблене
    6. Категорія
    7. Відгук
"""
# TODO категорія