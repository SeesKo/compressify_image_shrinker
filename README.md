# Compressify

Compressify is a web application designed for image compression. It allows users to upload images, select the desired compression level, compress the images, and download the compressed versions. Additionally, the application keeps track of uploaded, compressed, and deleted files in a SQLite database.


## Features

- Upload images either directly or through URLs
- Choose from various compression levels (10, 25, 50, 75, or 90)
- View compression progress
- Download compressed images
- Delete images from the system


## Technologies Used

- Flask: A micro web framework for Python
- SQLAlchemy: An SQL toolkit and Object-Relational Mapping (ORM) library for Python
- APScheduler: A Python library for scheduling tasks
- PIL (Python Imaging Library): A library for opening, manipulating, and saving many different image file formats
- SQLite: A lightweight relational database management system
- HTML/CSS: For the frontend user interface


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/compressify.git
    ```

2. Navigate to the project directory:

    ```bash
    cd compressify
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Access the application in your web browser at [http://localhost:5000](http://localhost:5000).


## Usage

1. Navigate to the homepage.
2. Upload an image file or provide a URL to an image.
3. Select the desired compression level using the slider.
4. Click the "Compress" button to initiate the compression process.
5. Monitor the progress of the compression if needed.
6. Once the compression is complete, download the compressed image.
7. Optionally, delete images from the system using the provided functionality.


## Database Schema

The application uses a SQLite database to store information about uploaded and compressed images. The database schema is as follows:

    ImageRecord
    -----------
    id (Primary Key, Integer)
    original_filename (String)
    compressed_filename (String)
    original_size (Integer)
    compressed_size (Integer)
    upload_time (DateTime)


## Contributors

Erick Siiko


## License

This project is proprietary software and all rights are reserved. You may not copy, distribute, or modify this software without explicit permission from the author.

For inquiries regarding licensing or use of this software, please contact this account.


## Support

For support or inquiries, please contact this account.
