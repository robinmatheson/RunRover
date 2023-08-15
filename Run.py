from app import db
# from flask_sqlalchemy import Integer, String, Float

class Run(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    run_type = db.Column(db.String, nullable = False)
    date = db.Column(db.String(10), nullable = False)
    time = db.Column(db.String(8), nullable = False)
    distance = db.Column(db.Float, nullable = False)
    pace = db.Column(db.String(8), nullable = False)
    difficulty = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return 'f<{self.run_type}, {self.date}>'