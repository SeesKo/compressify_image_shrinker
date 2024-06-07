# Compressify


<p align="center">
  <img src="static/images/form_logo.png" alt="Compressify-logo"/>
</p>


## Introduction
Compressify is a web application designed to compress images, making them smaller and more manageable without significant loss in quality. This application allows users to upload images directly from their device or via URL, select the desired compression level, compress the images, and download the compressed versions.

You can check out the deployed site here: [Compressify](https://compressify.onrender.com/).

For a detailed overview of the project's development, read the final project blog article here: [Compressify Project Blog Article](link-to-blog-article).

**Author:**  
Erick Siiko: [LinkedIn](https://www.linkedin.com/in/siiko/)


## Features

- Upload images either directly or through URLs
- Choose from various compression levels (10, 25, 50, 75, or 90)
- View compression progress
- Download compressed images
- Delete images from the system


## Technologies Used

- **Flask:** A micro web framework for Python
- **SQLAlchemy:** An SQL toolkit and Object-Relational Mapping (ORM) library for Python
- **APScheduler:** A Python library for scheduling tasks
- **Pillow (Python Imaging Library):** A library for opening, manipulating, and saving many different image file formats
- **SQLite:** A lightweight relational database management system
- **HTML, CSS, JavaScript:** For the frontend user interface
- **HTTP Requests:** Requests library for handling URL uploads


## Installation

1. Clone the repository.

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

5. Access the application in your web browser at `http://localhost:5000`.


## Project Structure

- **app.py:** Main application file that initializes Flask, sets up the database, and registers blueprints.
- **routes/:** Contains route definitions for handling different HTTP requests.
    - `main_routes.py`: Defines the main routes for the application.
    - `compression_routes.py`: Defines routes for image compression-related operations.
    - `download_routes.py`: Defines routes for downloading and deleting images.
- **services/:** Contains business logic and helper functions.
    - `compression_service.py`: Functions for compressing images and saving records.
- **static/:** Contains static files like CSS and JavaScript.
    - `script.js`: Handles frontend interactions for uploading and compressing images.
    - `download.js`: Handles frontend interactions for downloading and deleting images.
- **templates/:** Contains HTML templates.
    - `index.html`: Main page template.
    - `download.html`: Template for the download page.
- **config.py:** Configuration settings for the application.


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


## Related Projects

Some websites and resources that inspired Compressify's design:

- **FreeConvert** - Inspiration for the user interface and layout.
- **ResizePixel** - Ideas for certain features and functionalities.


## License

This project is proprietary software and all rights are reserved. You may not copy, distribute, or modify this software without explicit permission from the author.

For inquiries regarding licensing or use of this software, please contact this account.


---

This README file provides a comprehensive overview of the Compressify project, including its features, setup instructions, and project structure.
