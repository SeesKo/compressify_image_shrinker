"""
Defines the database model for storing image records.
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class ImageRecord(db.Model):
    """
    Model for storing image records in the database.
    """
    # Define database columns for image records
    id = db.Column(db.Integer, primary_key=True)
    original_filename = db.Column(db.String(100))
    compressed_filename = db.Column(db.String(100))
    original_size = db.Column(db.Integer)
    compressed_size = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)