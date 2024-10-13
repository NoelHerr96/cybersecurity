function genToken() {
  // Create a new XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Configure it: POST-request for the URL /token
  xhr.open('POST', '/generate-OTP', true);

  // Set up a request header to indicate the type of content being sent
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

  // Handle the response
  xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 300) {
      console.log('Success:');
    } else {
      console.error('Error:');
    }
  };

  // Send the request
  xhr.send();
}