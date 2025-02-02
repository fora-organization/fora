from flask import Blueprint, request, render_template, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash
from models import Session, User

register_routes = Blueprint('register_routes', __name__)


@register_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        session = Session()
        new_user = User(email=email, password=hashed_password)

        try:
            session.add(new_user)
            session.commit()
            flash('Реєстрація успішна! Ви можете увійти.', 'success')
            return redirect(url_for('login_routes.login'))
        except IntegrityError:
            session.rollback()
            flash('Користувач з таким email вже існує.', 'error')
        finally:
            session.close()

    return render_template('register.html')
