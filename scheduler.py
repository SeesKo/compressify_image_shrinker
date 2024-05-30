"""
Manages the periodic deletion of old image records
from the database and filesystem.
"""
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from models import db, ImageRecord
import atexit
import os


def delete_old_images():
    """
    Delete images older than 30 minutes from the database and filesystem.
    """
    # Calculate the time threshold for deleting old images
    now = datetime.utcnow()
    time_threshold = now - timedelta(minutes=30)
    # Query for old image records from the database
    old_records = ImageRecord.query.filter(ImageRecord.upload_time < time_threshold).all()
    # Iterate through old records and delete corresponding files and database records
    for record in old_records:
        try:
            if os.path.exists(record.original_filename):
                os.remove(record.original_filename)
            if os.path.exists(record.compressed_filename):
                os.remove(record.compressed_filename)
            db.session.delete(record)
        except Exception as e:
            print(f"Error deleting image: {e}")

    db.session.commit()


def start_scheduler(app):
    """
    Start the background scheduler to delete old images periodically.

    Args:
        app: The Flask application instance.
    """
    # Create and configure a background scheduler
    scheduler = BackgroundScheduler()
    # Schedule the delete_old_images function to run every 30 minutes
    scheduler.add_job(func=delete_old_images, trigger="interval", minutes=30)
    scheduler.start()  # Start the scheduler
    # Register scheduler shutdown on application exit
    atexit.register(lambda: scheduler.shutdown())