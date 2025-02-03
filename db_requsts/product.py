from models import Product, Session


def get_all_products():
    with Session() as session:
        return session.query(Product).all()


def create_product(name: str, description: str, price: float, quantity: int, image_url: str, rating: float) -> Product:
    with Session() as session:
        product = Product(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            image_url=image_url,
            rating=rating
        )
        session.add(product)
        session.commit()
        return product


def test_create_product():
    with Session() as session:
        product = Product(
            name="name",
            description="description",
            price=5.5,
            quantity=5,
            image_url="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png",
            rating=4.5
        )
        session.add(product)
        session.commit()

        print(f"-------------------------------------- {product.id}")

        product_from_db = session.query(Product).filter_by(id = product.id).first()

        if product_from_db:
            print("\n🔍 Отримано продукт з бази:")
            print(f"   🆔 ID: {product_from_db.id}")
            print(f"   📌 Name: {product_from_db.name}")
            print(f"   📝 Description: {product_from_db.description}")
            print(f"   💰 Price: ${product_from_db.price}")
            print(f"   📦 Quantity: {product_from_db.quantity}")
            print(f"   🖼 Image URL: {product_from_db.image_url}")
            print(f"   ⭐ Rating: {product_from_db.rating}")
        else:
            print("❌ Продукт не знайдено!")


if __name__ == "__main__":
    test_create_product()


# TODO добавити перевірки, чи всі поля введені
