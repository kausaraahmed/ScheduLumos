document.getElementById('run-algo').addEventListener('click', function () {
    const arrivalTimes = document.getElementById('arrival-time').value;
    const burstTimes = document.getElementById('burst-time').value;
    const timeQuantum = document.getElementById('time-quantum').value;

    fetch('/round-robin', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `arrival-time=${encodeURIComponent(arrivalTimes)}&burst-time=${encodeURIComponent(burstTimes)}&time-quantum=${encodeURIComponent(timeQuantum)}`
    })
        .then(response => response.text())
        .then(data => {
            document.getElementById('result').innerHTML = `<pre>${data}</pre>`;
            const downloadLink = document.getElementById('download-link');
            const blob = new Blob([data], { type: 'text/plain' });
            const url = URL.createObjectURL(blob);
            downloadLink.href = url;
            downloadLink.download = 'round_robin_result.txt';
            downloadLink.style.display = 'flex';
            send_compare.style.display = 'flex';
        })
});
document.getElementById('send_compare').addEventListener('click', function () {
    const arrivalTimes = document.getElementById('arrival-time').value;
    const burstTimes = document.getElementById('burst-time').value;
    const timeQuantum = document.getElementById('time-quantum').value;

    fetch('/compare', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `arrival-time=${arrivalTimes}&burst-time=${burstTimes}&time-quantum=${timeQuantum}`
    })
        .then(response => {
            if (response.ok) {
                window.location.href = "/compare";
            } else {
                console.error("Failed to send data to compare page.");
            }
        }).catch(error => console.error('Error:', error));
});