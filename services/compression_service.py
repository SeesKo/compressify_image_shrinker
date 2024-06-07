"""
Compresses images and saves their metadata to the database.
"""
from datetime import datetime, timezone
from flask import current_app
from models import db, ImageRecord
from PIL import Image
import os


def compress_image(filepath, compression_level=50):
    """
    Compresses the image at the given filepath with the specified compression level.

    Args:
        filepath (str): The path to the image file to be compressed.
        compression_level (int): The compression level ranging from 10 to 90.

    Returns:
        str: The filepath of the compressed image.
    """
    image = Image.open(filepath)

    # Determine quality based on compression level
    quality = 50
    if compression_level == 10:
        quality = 90
    elif compression_level == 25:
        quality = 75
    elif compression_level == 50:
        quality = 50
    elif compression_level == 75:
        quality = 25
    elif compression_level == 90:
        quality = 10

    # Resize the image based on quality
    new_width = int(image.width * (quality / 100))
    new_height = int(image.height * (quality / 100))
    compressed_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Save the compressed image
    compressed_filename = os.path.join(current_app.config['COMPRESSED_FOLDER'], os.path.basename(filepath))
    compressed_image.save(compressed_filename)

    return compressed_filename


def save_image_record(original_filename, compressed_filepath):
    """
    Saves the image record to the database.

    Args:
        original_filename (str): The name of the original image file.
        compressed_filepath (str): The filepath of the compressed image.
    """
    # Get file sizes and current time
    original_path = os.path.join(current_app.config['UPLOAD_FOLDER'], original_filename)
    compressed_size = os.path.getsize(compressed_filepath)
    original_size = os.path.getsize(original_path)
    upload_time = datetime.now(timezone.utc)

    # Create and save the ImageRecord object
    record = ImageRecord(
        original_filename=original_filename,
        compressed_filename=os.path.basename(compressed_filepath),
        original_size=original_size,
        compressed_size=compressed_size,
        upload_time=upload_time
    )
    db.session.add(record)
    db.session.commit()
