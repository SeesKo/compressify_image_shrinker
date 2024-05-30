"""
Handles rendering the index page of the application.
"""
from flask import Blueprint, render_template

# Create a Blueprint object: 'main_bp'
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """
    Render the index page.

    Returns:
        Rendered HTML template for the index page.
    """
    return render_template('index.html')