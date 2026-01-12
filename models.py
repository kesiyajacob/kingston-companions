from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    interests = db.Column(db.String, nullable=False)  # comma-separated keywords
    bio = db.Column(db.String, nullable=False) 

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    keywords = db.Column(db.Text)
    description = db.Column(db.Text)
    
    
