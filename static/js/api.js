// Handling Dropbox Chooser
document.getElementById('fromDropbox').addEventListener('click', function() {
    Dropbox.choose({
        success: function(files) {
            // Handle the selected files
            console.log(files);
        },
        cancel: function() {
            // Optional: Handle when the user cancels the selection
        },
        linkType: 'direct', // Choose either 'preview' or 'direct'
        multiselect: false, // Set to true if you want to allow multiple file selection
        extensions: ['.jpg', '.jpeg', '.png', '.gif'] // Optional: Specify allowed file extensions
    });
});

// Handling Google Drive Chooser
var developerKey = 'YOUR_DEVELOPER_KEY';
var clientId = 'YOUR_CLIENT_ID';
var scope = ['https://www.googleapis.com/auth/drive.file'];
var pickerApiLoaded = false;
var oauthToken;

function onApiLoad() {
    gapi.load('auth', {'callback': onAuthApiLoad});
    gapi.load('picker', {'callback': onPickerApiLoad});
}

function onAuthApiLoad() {
    window.gapi.auth.authorize(
        {
            'client_id': clientId,
            'scope': scope,
            'immediate': false
        },
        handleAuthResult);
}

function onPickerApiLoad() {
    pickerApiLoaded = true;
}

function handleAuthResult(authResult) {
    if (authResult && !authResult.error) {
        oauthToken = authResult.access_token;
        createPicker();
    }
}

function createPicker() {
    if (pickerApiLoaded && oauthToken) {
        var picker = new google.picker.PickerBuilder()
            .addView(google.picker.ViewId.DOCS)
            .setOAuthToken(oauthToken)
            .setDeveloperKey(developerKey)
            .setCallback(pickerCallback)
            .build();
        picker.setVisible(true);
    }
}

function pickerCallback(data) {
    if (data.action == google.picker.Action.PICKED) {
        var file = data.docs[0];
        console.log("Selected file: ", file);
        // Handle the selected file here
    }
}

document.getElementById('fromGoogleDrive').onclick = function() {
    onApiLoad();
};

// Handling URL Chooser
