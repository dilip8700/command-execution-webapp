document.getElementById('commandForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const command = document.getElementById('command').value;
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = '<p>Running command: <code>' + command + '</code></p>';
    
    fetch('/cgi-bin/command_exec.py', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'command=' + encodeURIComponent(command),
    })
    .then(response => response.text())
    .then(data => {
        outputDiv.innerHTML += data;
    })
    .catch(error => {
        outputDiv.innerHTML += '<p>Error: ' + error + '</p>';
    });
});

