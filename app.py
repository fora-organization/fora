from crypt import methods

from flask import Flask, render_template, request, redirect, url_for, flash, session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from models import *


app = Flask(__name__)

app.secret_key = "gasfhzx"


from routes import *


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        db_session = Session()
        new_user = User(email=email, password=hashed_password)

        try:
            db_session.add(new_user)
            db_session.commit()
            flash('Реєстрація успішна! Ви можете увійти.', 'success')
            return redirect(url_for('login'))
        except IntegrityError:
            db_session.rollback()
            flash('Користувач з таким email вже існує.', 'error')
        finally:
            db_session.close()

    return render_template('register.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db_session = Session()
        user = db_session.query(User).filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["user_name"] = user.first_name

            flash('Успішний вхід!', 'success')
            return redirect(url_for('products_route'))
        else:
            flash('Невірний email або пароль.', 'error')

        db_session.close()

    return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route("/cart")
def cart():
    if "user_id" not in session:
        flash("Увійдіть будь ласка в аккаунт", "warning")
        return redirect(url_for("login"))

    with Session() as db_session:
        user = db_session.query(User).get(session["user_id"])
        return render_template("cart.html", cart = user.cart)


@app.route("/add_to_cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    user_id = 1
    quantity = 1

    with Session() as db_session:
        user = db_session.get(User).where(User.id == user_id).first()
        product = db_session.get(Product, product_id)

        if user and product:
            if product in user.cart:
                # redirect(url_for("cart"))
                for item in user.cart:
                    if item.id == product.id:
                        item.quantity += quantity
            else:
                user.cart.append(product)
                product.quantity = quantity

            db_session.commit()

    return redirect(url_for("cart"))


@app.route("/remove_from_cart/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    user_id = 1

    with Session() as db_session:
        user = db_session.get(User).where(User.id == user_id).first()
        product = db_session.get(Product, product_id)

        if user and product:
            if product in user.cart:
                user.cart.remove(product)
                db_session.commit()

    return redirect(url_for("cart"))






if __name__ == "__main__":
    app.run(debug=True)