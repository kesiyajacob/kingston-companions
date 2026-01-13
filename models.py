from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable = False )
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    interests = db.Column(db.String, nullable=False)  # comma-separated keywords
    bio = db.Column(db.String, nullable=False) 

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    keywords = db.Column(db.Text)
    description = db.Column(db.Text)
    image = db.Column(db.String(200))
    
    
