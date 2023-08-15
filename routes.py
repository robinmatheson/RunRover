from app import app
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