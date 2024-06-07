"""
Handles download and deletion of compressed image
files and their corresponding database records.
"""
from flask import Blueprint, send_file, jsonify, current_app
from models import ImageRecord, db
from sqlalchemy.exc import SQLAlchemyError
import os

# Create Blueprint object
download_bp = Blueprint('download', __name__)


@download_bp.route('/download/<filename>')
def download_file(filename):
    """
    Handle downloading of the compressed file.

    Args:
        filename (str): Name of the file to be downloaded.

    Returns:
        The file as an attachment or a JSON error message.
    """
    try:
        # Construct the file path for the compressed file
        file_path = os.path.join(current_app.config['COMPRESSED_FOLDER'], filename)
        # Send the compressed file as an attachment
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        # Return a JSON error message if the file is not found
        return jsonify({'error': 'File not found'}), 404


@download_bp.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    """
    Handle deletion of the original and compressed files and their database record.

    Args:
        filename (str): Name of the file to be deleted.

    Returns:
        JSON response indicating success or an error message.
    """
    try:
        # Find the corresponding image record in the database
        record = ImageRecord.query.filter_by(compressed_filename=filename).first()
        if record:
            # Construct paths for the original and compressed files
            original_path = os.path.join(current_app.config['UPLOAD_FOLDER'], record.original_filename)
            compressed_path = os.path.join(current_app.config['COMPRESSED_FOLDER'], record.compressed_filename)
            # Remove the original and compressed files if they exist
            if os.path.exists(original_path):
                os.remove(original_path)
            if os.path.exists(compressed_path):
                os.remove(compressed_path)
            # Delete the image record from the database
            db.session.delete(record)
            db.session.commit()
            return jsonify({'success': True})  # Return success message
        else:
            return jsonify({'error': 'File not found'}), 404  # File not found error
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500  # Database error
