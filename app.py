from flask import Flask, render_template, request, redirect, url_for
from models import *


app = Flask(__name__)

from routes import *

if __name__ == "__main__":
    drop_db()
    create_db()
    app.run(debug=True)