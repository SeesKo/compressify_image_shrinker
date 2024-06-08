document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const compressionMeter = document.getElementById('compressionMeter');
    const progressBar = compressionMeter.querySelector('.progress-bar');
    const filename = document.getElementById('resultFileName').textContent;

    // Set up interval to periodically fetch progress
    const progressUpdateInterval = setInterval(() => {
        fetch(`/progress/${filename}`)
            .then(response => response.json())
            .then(data => {
                if (data.progress >= 0 && data.progress <= 100) {
                    progressBar.style.width = `${data.progress}%`;
                }
                if (data.progress === 100) {
                    clearInterval(progressUpdateInterval);
                    compressionMeter.textContent = 'DONE';
                    compressionMeter.classList.add('done');
                }
            })
            .catch(error => {
                console.error('Error fetching progress:', error);
            });
    }, 1000); // Fetch progress every second

    // Event handlers
    document.getElementById('saveToDevice').onclick = function() {
        window.location.href = '/download/' + filename;
    }

    document.getElementById('compressMoreFiles').onclick = function() {
        window.location.href = '/';
    }

    document.getElementById('deleteFiles').onclick = function() {
        const confirmationText = 'Are you sure you want to delete this file?';
        const confirmed = window.confirm(confirmationText);
        if (confirmed) {
            // Delete file
            fetch('/delete/' + filename, { method: 'DELETE' })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('File deleted.');
                        window.location.href = '/';
                    } else {
                        alert('Delete failed: ' + data.error);
                    }
                })
                .catch(error => {
                    alert('Error: ' + error.message);
                });
        }
    }

    // Set the current year in the footer
    const currentYear = new Date().getFullYear();
    document.getElementById('currentYear').textContent = currentYear;
});
