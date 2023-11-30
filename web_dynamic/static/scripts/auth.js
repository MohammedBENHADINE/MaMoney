document.addEventListener('DOMContentLoaded', function() {
function showMessage(message, isSuccess) {
  const messageBox = document.getElementById('message-box');
  messageBox.textContent = message;
  messageBox.className = isSuccess ? 'text-green-500' : 'text-red-500';
  messageBox.style.display = 'block';
}

function handleLogin(event) {
  event.preventDefault();

  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;
  let errorDetected = false;

  fetch('http://localhost:5000/api/v1/user/login', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
  })
    .then(response => {
        errorDetected = response.status;
        return response.json()
    })
    .then(data =>{
        if (errorDetected == 400)
            showMessage(data.error, false);
        else
        {
            showMessage("Login Successful !", true);
            window.location.href = '/config?id='+data.id;
        }

    })
  .catch(error => {
      console.error('Error:', error);
      showMessage('Error during login.', false);
  });
}

function handleSignUp(event) {
  event.preventDefault();

  const username = document.getElementById('signup-username').value;
  const email = document.getElementById('signup-email').value;
  const password = document.getElementById('signup-password').value;
  const confirmPassword = document.getElementById('signup-confirm-password').value;

  if (password === confirmPassword) {
      fetch('http://localhost:5000/api/v1/users', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, email, password, profileDetails: 'Some details' }),
      })
      .then(response => response.json())
      .then(data => {
          // Handle the response data as needed
          console.log(data);
          showMessage(data.error, true);
      })
      .catch(error => {
          console.error('Error:', error);
          showMessage('Error during sign up.', false);
      });
  } else {
      showMessage('Passwords do not match.', false);
  }
}
document.getElementById('login-form').addEventListener('submit', handleLogin);
document.getElementById('signup-form').addEventListener('submit', handleSignUp);
});
