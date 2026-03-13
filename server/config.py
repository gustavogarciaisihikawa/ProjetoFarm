from flask_sqlalchemy import SQLAlchemy

# Initialize the database

db = SQLAlchemy()

# Configuration settings
class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False