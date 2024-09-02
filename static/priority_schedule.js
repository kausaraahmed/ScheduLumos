document.getElementById('run-algo').addEventListener('click', function () {
    const arrivalTimes = document.getElementById('arrival-time').value;
    const burstTimes = document.getElementById('burst-time').value;
    const priority = document.getElementById('priority').value;

    fetch('/priority-scheduling', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `arrival-time=${encodeURIComponent(arrivalTimes)}&burst-time=${encodeURIComponent(burstTimes)}&priority=${encodeURIComponent(priority)}`
    })
        .then(response => response.text())
        .then(data => {
            document.getElementById('result').innerHTML = `<pre>${data}</pre>`;
            const downloadLink = document.getElementById('download-link');
            const blob = new Blob([data], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            downloadLink.href = url;
            downloadLink.download = 'priority_scheduling_result.txt';
            downloadLink.style.display = 'flex';
            send_compare.style.display = 'flex';
        })
        .catch(error => console.error('Error:', error));
});
document.getElementById('send_compare').addEventListener('click', function () {
    const arrivalTimes = document.getElementById('arrival-time').value;
    const burstTimes = document.getElementById('burst-time').value;
    const priority = document.getElementById('priority').value;

    fetch('/compare', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `arrival-time=${encodeURIComponent(arrivalTimes)}&burst-time=${encodeURIComponent(burstTimes)}&priority=${encodeURIComponent(priority)}`
    })
        .then(response => {
            if (response.ok) {
                window.location.href = "/compare";
            } else {
                console.error("Failed to send data to compare page.");
            }
        }).catch(error => console.error('Error:', error));
});
