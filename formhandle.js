document.querySelector('form').addEventListener('submit', function (event) {
  event.preventDefault();
  const formData = new FormData(event.target);
  const inputElement = event.target.querySelector('input[type="text"]');
  
  // Include the identifier in the data to send to the server
  formData.append('identifier', identifier);
  
  fetch('http://127.0.0.1:7000/order', {
      method: 'POST',
      body: JSON.stringify(Object.fromEntries(formData)),
      headers: {
          'Content-Type': 'application/json',
      },
  })
  .then(response => response.text())
  .then(data => console.log(data));
});
