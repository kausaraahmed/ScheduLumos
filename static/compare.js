function runAlgorithm(algorithm) {
    const timeQuantum = document.getElementById('time-quantum') ? document.getElementById('time-quantum').value : '';
    const priority = document.getElementById('priority') ? document.getElementById('priority').value : '';

    fetch(`/compare`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `algo=${algorithm}&tQ=${timeQuantum}&priority=${priority}`
    })
        .then(response => response.text())
        .then(data => {
            const [tat, wt] = extractor(data);

            if (tat && wt) {
                document.getElementById(`${algorithm}-tat`).innerText = 'Avg. TAT time: ' + tat + 's';
                document.getElementById(`${algorithm}-wt`).innerText = 'Avg. Wt time: ' + wt + 's';
            } else {
                document.getElementById(`${algorithm}-tat`).innerText = 'Error';
                document.getElementById(`${algorithm}-wt`).innerText = 'Error';
            }
        })
        .catch(error => console.error('Error:', error));
}

function extractor(text) {
    const waitingTimeMatch = text.match(/Average Waiting Time: (\d+\.\d+)/);
    const turnaroundTimeMatch = text.match(/Average Turnaround Time: (\d+\.\d+)/);

    const wt = waitingTimeMatch ? waitingTimeMatch[1] : null;
    const tat = turnaroundTimeMatch ? turnaroundTimeMatch[1] : null;
    return [tat, wt]
}
