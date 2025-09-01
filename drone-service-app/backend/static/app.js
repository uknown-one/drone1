document.getElementById('drone-form').addEventListener('submit', function (event) {
  event.preventDefault();

  const location = document.getElementById('location').value;
  const missionType = document.getElementById('mission-type').value;

  // Prepare request data
  const requestData = {
    location: location,
    mission_type: missionType
  };

  fetch('/api/start_mission', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(requestData),
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('status-message').textContent = `Mission ID: ${data.mission_id} started successfully!`;
  })
  .catch(error => {
    document.getElementById('status-message').textContent = 'An error occurred. Please try again.';
    console.error('Error:', error);
  });
});
