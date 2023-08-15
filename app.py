from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os
from config import Config

app = Flask(__name__)

# app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:sv6FYf*6B@localhost/runroverDB'
# SQLAlchemy instance
db = SQLAlchemy(app)

# with app.app_context():
#     db.reflect()

from Run import Run

@app.route('/')

# to test the database connection
# def testdb():
#     try:
#         db.session.query("1").from_statement(text("SELECT 1")).all()
#         return '<h1>It works.</h1>'
#     except:
#         return '<h1>Something is broken.</h1>'
        
def index():
    runs = Run.query.all()
    return render_template('index.html', runs=runs)

if __name__ == "__main__":
    app.run(debug=True)
