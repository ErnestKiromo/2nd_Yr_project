document.getElementById('signupForm').addEventListener('submit', function(event) {
            event.preventDefault();  // Prevent form submission

            // Get form input values
            let username = document.getElementById('username').value;
            let email = document.getElementById('email').value;
            let password = document.getElementById('password').value;

            // Create user data object
            let userData = {
                username: username,
                email: email,
                password: password
            };
            for (let key in userData) {
                if (userData.hasOwnProperty(key)) {
                    let value = userData[key];
                    console.log(`${key}: ${value}`);
                }
            }
            // Send POST request to backend
            fetch('http://localhost:8001/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(userData)
            })
            .then(response => response.json())
            .then(data => {
                console.log('Signup successful:', data);
                if (data && data.message && data.message === "User signed up successfully") {
                   window.location.pathname = "/dashboard.html";
                }       
                // Optionally, perform any actions after successful signup (e.g., redirect to another page)
            })
            .catch(error => {
                console.error('Signup failed:', error);
                // Optionally, display an error message to the user
            });
        });
        

// get user with id
function get_user(id) {
fetch('http://127.0.0.1:8001/users/{id}')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Handle the data returned from the API
    console.log(data);
    // Now you can use the data in your JavaScript code
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There was a problem with the fetch operation:', error);
  });
}

//get all users
function get_users() {
fetch('http://127.0.0.1:8001/all-users')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    // Handle the data returned from the API
    // console.log(data);
    return data;
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('There was a problem with the fetch operation:', error);
  });
}


