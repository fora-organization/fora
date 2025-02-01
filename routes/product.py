from flask import Flask, render_template, request, jsonify

from app import app
from db_requsts import create_product


@app.route("/create_product", methods=['GET', 'POST'])
def create_product_route():
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

    return render_template('create_product.html') #TODO