from database import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=True)
    description = db.Column(db.Text, nullable=True)
    deadline = db.Column(db.String(20), nullable=True)
    priority = db.Column(db.Integer, nullable=False, default=3)
    completed = db.Column(db.Boolean, default=False)
