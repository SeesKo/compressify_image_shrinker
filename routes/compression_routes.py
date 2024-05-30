"""
Handles image upload, compression, progress tracking, and rendering
the download page for the compressed images.
"""
from flask import Blueprint, request, jsonify, render_template, current_app
from services.compression_service import compress_image, save_image_record
from werkzeug.utils import secure_filename
import os
import requests


compression_bp = Blueprint('compression', __name__)


@compression_bp.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file or URL upload and compress the image.

    Returns:
        JSON response with the compressed image filename or an error message.
    """
    if 'file' in request.files:
        # Process file upload
        file = request.files['file']
        compression_level = int(request.form.get('compressionRange', 50))

        # Error if no file selected
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Error if non-image file uploaded
        if not file.content_type.startswith('image/'):
            return jsonify({'error': 'Only images are allowed.'}), 400

        # Securely save the file and compress it
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        compressed_filepath = compress_image(filepath, compression_level)
        save_image_record(filename, compressed_filepath)
        # Return compressed image filename
        return jsonify({'filename': os.path.basename(compressed_filepath)})

    elif 'url' in request.form:
        # Process URL upload
        file_url = request.form['url']
        response = requests.get(file_url)
        # Error if failed to download from URL
        if response.status_code != 200:
            return jsonify({'error': 'Failed to download file from URL'}), 400

        # Securely save the file and compress it
        filename = secure_filename(os.path.basename(file_url))
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)

        compression_level = int(request.form.get('compressionRange', 50))
        compressed_filepath = compress_image(filepath, compression_level)
        save_image_record(filename, compressed_filepath)
        # Return compressed image filename
        return jsonify({'filename': os.path.basename(compressed_filepath)})

    # Error if neither file nor URL provided
    else:
        return jsonify({'error': 'No file or URL provided'}), 400


@compression_bp.route('/progress/<filename>')
def get_compression_progress(filename):
    """
    Mock endpoint to get the compression progress of a file.

    Args:
        filename (str): Name of the file being compressed.

    Returns:
        JSON response with the progress percentage.
    """
    progress = len(filename) * 10
    return jsonify({'progress': min(progress, 100)})


@compression_bp.route('/results/<filename>')
def compression_results(filename):
    """
    Render the download page for a compressed file.

    Args:
        filename (str): Name of the compressed file.

    Returns:
        Rendered HTML page for downloading the compressed file.
    """
    return render_template('download.html', filename=filename)