document.addEventListener('DOMContentLoaded', function () {
  // Find all the buttons with the 'data-id' attribute
  const userInput = document.getElementById("image1-number");
  const buttonsWithDataId = document.querySelectorAll('[data-id]');

   // Get references to the button and input field
  const increaseMinButton = document.getElementById("increaseMinButton");
  const image1NumberInput = document.getElementById("image1-number");

  buttonsWithDataId.forEach(function (button) {
      button.addEventListener('click', function (event) { // Add the event parameter
        // Prevent the default form submission behavior
        event.preventDefault();

        // Get the 'data-id' attribute value
        const dataId = button.getAttribute('data-id');
        console.log('Data-id:', dataId);
        
        // Get the 'image1-number' attribute value
        const enteredValue = userInput.value;
        console.log("User entered: " + enteredValue);
        
        // Get the current value of the min attribute
        const currentMin = parseInt(image1NumberInput.min);
        // Increase the min value (e.g., by 1)
        const newMin = currentMin + 1;
        // Set the new min value
        image1NumberInput.min = newMin;
        console.log("Updated min value: " + newMin);
        
        alert('Are you sure you want to send' + enteredValue + ' to address => ' + dataId)

        // Send an HTTP request to your Flask API at http://127.0.0.1:5000/
        fetch('http://127.0.0.1:7000/orders', { // Update the URL to your API endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ dataId: dataId, enteredValue: enteredValue }),
        })
        .then(response => response.json())
        .then(data => {
            // Handle the API response as needed
            console.log(data);
        })
        .catch(error => {
            console.error('API request failed:', error);
        });
      });
  });
});
