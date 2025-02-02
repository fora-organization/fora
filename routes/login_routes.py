from flask import Blueprint, request, render_template, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
from models import Session, User

login_routes = Blueprint('login_routes', __name__)

@login_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        session = Session()
        user = session.query(User).filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            flash('Успішний вхід!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Невірний email або пароль.', 'error')

        session.close()

    return render_template('login.html')
