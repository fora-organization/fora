from flask import Flask, render_template, request, redirect, url_for, flash, session
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from models import *


app = Flask(__name__)

app.secret_key = "gasfhzx"


from routes import *


if __name__ == "__main__":
    app.run(debug=True)