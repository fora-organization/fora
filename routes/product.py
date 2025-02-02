from flask import Flask, render_template, request, jsonify

from app import app
from db_requsts import create_product, get_all_products


@app.route("/create_product", methods=['GET', 'POST'])
def create_product_route():
    if request.method == 'GET':
        return render_template('create_product.html')

    if request.method == 'POST':
        data = request.json
        required_field = ("name", "description", "price", "quantity", "image_url", "rating")
        if not all(field in data for field in required_field):
            return jsonify({"error": "Missing required fields"}), 400

        create_product(
            data['name'],
            data['description'],
            data['price'],
            data['quantity'],
            data['image_url'],
            data['rating']
        )

        return render_template('create_product.html')


@app.route("/products", methods=['GET'])
def products_route():
   return render_template('products.html', products=get_all_products())