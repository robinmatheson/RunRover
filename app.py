from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html',
                            # runs = RUNS
                            )

if __name__ == "__main__":
    app.run(debug=True)
