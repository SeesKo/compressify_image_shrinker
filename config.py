"""
Defines configuration settings for the Flask application.
"""
import os


class Config:
    """
    Configuration class for the Flask application.
    """
    UPLOAD_FOLDER = 'uploads/'
    COMPRESSED_FOLDER = 'compressed/'
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB max upload size
    SQLALCHEMY_DATABASE_URI = 'sqlite:///compressify.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        """
        Initialize the application with required directories.

        Args:
            app: The Flask application instance.
        """
        # Create directories for uploaded & compressed images if they don't exist
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(Config.COMPRESSED_FOLDER, exist_ok=True)