// Detect base API URL dynamically
const API_BASE = window.location.origin; // e.g., http://127.0.0.1:5000 in dev, or your domain in prod

document.getElementById('drone-form').addEventListener('submit', function (event) {
  event.preventDefault();

  const location = document.getElementById('location').value;
  const missionType = document.getElementById('mission-type').value;

  const requestData = {
    location: location,
    mission_type: missionType
  };

  // Start mission
  fetch(`${API_BASE}/api/start_mission`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(requestData),
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('status-message').textContent =
      `Mission ID: ${data.mission_id} started successfully! Fetching status...`;

    // Fetch mission status automatically
    return fetch(`${API_BASE}/api/mission_status/${data.mission_id}`);
  })
  .then(response => response.json())
  .then(statusData => {
    document.getElementById('status-message').textContent +=
      ` Current status: ${statusData.status}`;
  })
  .catch(error => {
    document.getElementById('status-message').textContent =
      '❌ An error occurred. Please try again.';
    console.error('Error:', error);
  });
});
