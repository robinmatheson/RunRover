from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

import mysql.connector
import os
import pymysql

from config import Config

# SQLAlchemy instance
db = SQLAlchemy()
# initialize Flask app
app = Flask(__name__)
# configure app with (hidden) SQLAlchemy Database URI
app.config.from_object(Config)
db.init_app(app)

# model for run
class Run(db.Model):
    __tablename__ = 'runs'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable = False)
    date = db.Column(db.String(10), nullable = False)
    time = db.Column(db.String(8), nullable = False)
    distance = db.Column(db.Float, nullable = False)
    pace = db.Column(db.String(8), nullable = False)
    difficulty = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return 'f<{self.run_type}, {self.date}>'

#routes
@app.route('/')
# to test the database connection
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text
        
def index():
    runs = Run.query.all()
    return render_template('index.html', runs = runs)

if __name__ == "__main__":
    app.run(debug=True)
