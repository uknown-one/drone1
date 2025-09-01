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
    const statusDiv = document.getElementById('status-message');
    const missionId = data.mission_id;
    statusDiv.textContent = `Mission ID: ${missionId} started successfully!`;

   // Poll mission status every 3 seconds
    const interval = setInterval(() => {
      fetch(`${API_BASE}/api/mission_status/${missionId}`)
        .then(resp => resp.json())
        .then(statusData => {
          statusDiv.textContent = `Mission ID: ${missionId} | Status: ${statusData.status}`;

          // Stop polling if mission is completed
          if (statusData.status.toLowerCase() === 'completed') {
            clearInterval(interval);
          }
        })
        .catch(err => {
          statusDiv.textContent = 'Error fetching mission status.';
          console.error(err);
          clearInterval(interval);
        });
    }, 3000); // 3 seconds
  })
  .catch(error => {
    document.getElementById('status-message').textContent =
      '❌ An error occurred. Please try again.';
    console.error('Error:', error);
  });
});
