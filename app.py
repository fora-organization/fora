from flask import Flask, render_template, request, redirect, url_for
from models import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user_details():
    return render_template('user_details.html')


if __name__ == "__main__":
    create_db()
    app.run(debug=True)