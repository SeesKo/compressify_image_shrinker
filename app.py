"""
Initializes and configures the Flask application.
"""
from config import Config
from flask import Flask
from models import db
from routes.compression_routes import compression_bp
from routes.download_routes import download_bp
from routes.main_routes import main_bp
from scheduler import start_scheduler


def create_app():
    """
    Create and configure the Flask application.

    Returns:
        app: The configured Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)  # Initialize the database

    # Register blueprints for different routes
    app.register_blueprint(main_bp)
    app.register_blueprint(compression_bp)
    app.register_blueprint(download_bp)

    with app.app_context():
        db.create_all()  # Create database tables
        start_scheduler(app)  # Start the scheduler

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode