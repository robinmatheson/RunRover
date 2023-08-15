from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route('/')

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
