from models import (
    Product,
    Session
)

def get_all_products():
    with Session() as session:
        return session.query(Product).all()