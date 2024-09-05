document.getElementById('run-algo').addEventListener('click', function () {
    const arrivalTimes = document.getElementById('arrival-time').value;
    const burstTimes = document.getElementById('burst-time').value;

    fetch('/sjf-non-preemptive', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `arrival-time=${arrivalTimes}&burst-time=${burstTimes}`
    })
        .then(response => response.text())  // Expecting text here instead of JSON
        .then(data => {
            document.getElementById('result').innerHTML = `<pre>${data}</pre>`;
            const downloadLink = document.getElementById('download-link');
            const blob = new Blob([data], {type: 'text/plain'});
            const url = URL.createObjectURL(blob);
            downloadLink.href = url;
            downloadLink.download = 'sjf_preemptive_result.txt';
            downloadLink.style.display = 'flex';
            send_compare.style.display = 'flex';
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('send_compare').addEventListener('click', function () {
    const arrivalTimes = document.getElementById('arrival-time').value;
    const burstTimes = document.getElementById('burst-time').value;

    fetch('/compare', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `arrival-time=${encodeURIComponent(arrivalTimes)}&burst-time=${encodeURIComponent(burstTimes)}`
    })
        .then(response => {
            if (response.ok) {
                window.location.href = "/compare";
            } else {
                console.error("Failed to send data to compare page.");
            }
        }).catch(error => console.error('Error:', error));
});