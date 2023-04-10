from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), unique=True, nullable=False)
    answer = db.Column(db.String(50), unique=True, nullable=False)
    subject = db.Column(db.String(50), unique=False, nullable=False)
    
    def repr(self):
        return '<Questions %r>' % self.id


@app.route("/")
def home():
    return render_template()

if __name__ == "__main__":
    app.run(debug=True)