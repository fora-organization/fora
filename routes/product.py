from flask import (
    render_template
)

from app import (
    app,
)

from db_requsts import (
    get_all_products
)

@app.route('/products')
def show_all_products():
    products = get_all_products()
    return render_template('products.html', products=products)
