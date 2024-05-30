// Get DOM elements
const fileInput = document.getElementById('fileInput');
const fromDevice = document.getElementById('fromDevice');
const fromURL = document.getElementById('fromURL');
const fileInfo = document.getElementById('fileInfo');
const fileName = document.getElementById('fileName');
const fileSize = document.getElementById('fileSize');
const fileType = document.getElementById('fileType');
const removeFile = document.getElementById('removeFile');
const fileSummary = document.getElementById('fileSummary');
const fileCount = document.getElementById('fileCount');
const compressButton = document.getElementById('compressButton');
const settingsToggle = document.getElementById('settingsToggle');
const slider = document.getElementById('slider');
const compressionRange = document.getElementById('compressionRange');
const compressionValue = document.getElementById('compressionValue');

// Function to toggle the display of the Settings toggle button
function toggleSettingsButton(display) {
    settingsToggle.style.display = display ? 'inline-block' : 'none';
}

// Function to snap the slider to nearest calibration point
function snapToCalibration(value) {
    const calibrationPoints = [10, 25, 50, 75, 90];
    return calibrationPoints.reduce((prev, curr) => Math.abs(curr - value) < Math.abs(prev - value) ? curr : prev);
}

// Event handlers
fromDevice.onclick = function() {
    fileInput.click();
}

fromURL.onclick = function() {
    const url = prompt('Enter URL:');
    if (url === null) { // Check if user clicked Cancel
        return; // Exit the function if canceled
    } else if (url.trim() === '') { // Check if URL is empty after trimming whitespace
        alert('URL cannot be empty.');
        return;
    }

    console.log('Entered URL:', url);
    fileName.textContent = url;
    toggleSettingsButton(false); // Hide the Settings toggle button

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch file information');
            }
            const contentType = response.headers.get('Content-Type');
            if (!contentType || !contentType.startsWith('image/')) {
                throw new Error('URL does not point to an image');
            }
            return response.blob();
        })
        .then(blob => {
            const fileSizeValue = (blob.size / 1024).toFixed(2) + ' KB';
            const fileTypeValue = blob.type;
            console.log('File type:', fileTypeValue);
            fileSize.textContent = fileSizeValue;
            fileType.textContent = fileTypeValue;

            // Create a File object from the blob
            const file = new File([blob], url.split('/').pop(), { type: fileTypeValue });
            // Store the file in the file input
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            fileInput.files = dataTransfer.files;

            fileInfo.style.display = 'flex';
            fileSummary.style.display = 'flex';
            fileCount.textContent = '1 file added';
            toggleSettingsButton(true); // Show the Settings toggle button
        })
        .catch(error => {
            if (error.message === 'Failed to fetch file information') {
                alert('Failed to fetch file information. Please enter a valid URL.');
            } else if (error.message === 'URL does not point to an image') {
                alert('URL does not point to an image. Please enter a valid image URL.');
            } else if (error.message.includes('NetworkError')) {
                alert('URL not a valid image URL or could not be reached. Please make sure URL is correct and try again.');
            } else {
                alert('Error: ' + error.message);
                console.error('Error fetching file information:', error.message);
            }
        });
};

fileInput.onchange = function(event) {
    const file = event.target.files[0];
    if (file) {
        const truncatedFileName = file.name.length > 20 ? file.name.substring(0, 20) + '...' : file.name;
        fileName.textContent = truncatedFileName;
        fileSize.textContent = (file.size / 1024).toFixed(2) + ' KB';
        fileType.textContent = file.type;
        fileInfo.style.display = 'flex';
        fileSummary.style.display = 'flex';
        fileCount.textContent = '1 file added';
        toggleSettingsButton(true); // Show the Settings toggle button
    }
};

removeFile.onclick = function() {
    fileInput.value = '';
    fileInfo.style.display = 'none';
    fileSummary.style.display = 'none';
    slider.style.display = 'none';
    toggleSettingsButton(false); // Hide the Settings toggle button
};

compressButton.onclick = function() {
    const file = fileInput.files[0];

    if (file && file.type.startsWith('image/')) {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('compressionRange', compressionRange.value);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json().then(data => ({ status: response.status, body: data })))
        .then(({ status, body }) => {
            if (status === 413) {
                alert(body.error);  // Show the custom error message for large files
            } else if (status === 200) {
                window.location.href = '/results/' + body.filename;
            } else {
                alert('Upload failed: ' + body.error);
            }
        })
        .catch(error => {
            alert('Error: ' + error.message);
        });
    } else {
        alert('Sorry. Only images are allowed.');
    }
};

// Smooth toggle effect for the Settings toggle button
settingsToggle.addEventListener('click', function () {
    if (slider.style.display === 'none') {
        slider.style.display = 'block';
        settingsToggle.classList.add('revealed'); // Change button text to "Settings ⮟"
    } else {
        slider.style.display = 'none';
        settingsToggle.classList.remove('revealed'); // Change button text back to "Settings ⮞"
    }
});

// Event listener for slider input change
compressionRange.addEventListener('input', function() {
    this.value = snapToCalibration(this.value);
    compressionValue.textContent = this.value + '%';
});

// Event listener for slider change (mouse release)
compressionRange.addEventListener('change', function() {
    this.value = snapToCalibration(this.value);
    compressionValue.textContent = this.value + '%';
});