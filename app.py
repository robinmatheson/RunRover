from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
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

    def __init__(self, type, date, time, distance, pace, difficulty):
        self.type = type
        self.date = date
        self.time = time
        self.distance = distance
        self.pace = pace
        self.difficulty = difficulty

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
def home_page():
    runs = Run.query.all()
    return render_template('index.html', runs = runs)

# add run page
@app.route('/addrun')
def show_add_run_page():
    return render_template('addrun.html')

# 
@app.route('/addrun/add', methods=['POST'])
def add_run():
    # get data from add run form
    data = request.form

    type = data['type']
    date = data['date']
    time = data['time']
    distance = data['distance']
    pace = data['pace']
    difficulty = data['difficulty']

    # create Run object
    record = Run(type, date, time, distance, pace, difficulty)
    
    # store this data in db
    db.session.add(record)
    db.session.commit()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
