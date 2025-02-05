from flask import request, render_template, redirect, url_for, flash, session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
from models import Session, User

from app import app

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
            return redirect(url_for('default'))
        else:
            flash('Невірний email або пароль.', 'error')

        db_session.close()

    return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))