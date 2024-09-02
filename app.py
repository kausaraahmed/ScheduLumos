from flask import Flask, render_template, request
from fcfs import FCFS
from SJF_nonPreemptive import SJF_nonPreemtive
from SJF_Preemptive import SJF_Preemtive
from priority_scheduling import Priority_Scheduling
from round_robin import Round_Robin

app = Flask(__name__)


# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')


# Route for the SJF Non-Preemptive Algorithm page
@app.route('/fcfs', methods=['GET', 'POST'])
def fcfs():
    if request.method == 'POST':
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')

        return run_fcfs(arrival_times, burst_times)

    return render_template('fcfs.html')


def run_fcfs(arrival_times, burst_times):
    try:
        arrival_times = list(map(int, arrival_times.strip().split(' ')))
        burst_times = list(map(int, burst_times.strip().split(' ')))
        n = len(arrival_times)
        processes = list(range(n))

        if n != len(burst_times):
            raise Exception("Number of Arrival Time and Burst Time must be equal.")

        scheduler = FCFS()
        result = scheduler.find_average_time(processes, n, burst_times, arrival_times)
        return result

    except Exception as error:
        result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
        return result


# Route for the SJF Non-Preemptive Algorithm page
@app.route('/sjf-non-preemptive', methods=['GET', 'POST'])
def sjf_non_preemptive():
    if request.method == 'POST':
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')
        result = run_sjfnp(arrival_times, burst_times)

        return result

    return render_template('sjf_non_preemptive.html')


def run_sjfnp(arrival_times, burst_times):
    try:
        arrival_times = list(map(int, arrival_times.strip().split(' ')))
        burst_times = list(map(int, burst_times.strip().split(' ')))
        n = len(arrival_times)
        processes = list(range(n))

        if n != len(burst_times):
            raise Exception("Number of Arrival Time and Burst Time must be equal.")

        scheduler = SJF_nonPreemtive()
        result = scheduler.findAverageTime(n, processes, burst_times, arrival_times)
        return result

    except Exception as error:
        result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
        return result


# Route for the SJF Preemptive Algorithm page
@app.route('/sjf-preemptive', methods=['GET', 'POST'])
def sjf_preemptive():
    if request.method == 'POST':
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')

        return run_sjfp(arrival_times, burst_times)

    return render_template('sjf_preemptive.html')


def run_sjfp(arrival_times, burst_times):
    try:
        arrival_times = list(map(int, arrival_times.strip().split(' ')))
        burst_times = list(map(int, burst_times.strip().split(' ')))
        n = len(arrival_times)
        processes = list(range(n))

        if n != len(burst_times):
            raise Exception("Number of Arrival Time and Burst Time must be equal.")

        scheduler = SJF_Preemtive()
        result = scheduler.findAverageTime(n, processes, burst_times, arrival_times)
        return result

    except Exception as error:
        result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
        return result


# Route for the Priority Scheduling Algorithm page
@app.route('/priority-scheduling', methods=['GET', 'POST'])
def priority_scheduling():
    if request.method == 'POST':
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')
        priority = request.form.get('priority')

        return run_priority(arrival_times, burst_times, priority)

    return render_template('priority_scheduling.html')


def run_priority(arrival_times, burst_times, priority):
    try:
        arrival_times = list(map(int, arrival_times.strip().split(' ')))
        burst_times = list(map(int, burst_times.strip().split(' ')))
        n = len(arrival_times)
        processes = list(range(n))
        if priority == '' or priority is None:
            priority = list(range(n))
        else:
            priority = list(map(int, priority.strip().split(' ')))

        if not (n == len(burst_times) == len(priority)):
            raise Exception("Number of Arrival Time, Burst Time and Priority must be equal.")

        scheduler = Priority_Scheduling()
        result = scheduler.priority_scheduling(processes, arrival_times, burst_times, priority)
        return result

    except Exception as error:
        result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
        return result


# Route for the Round Robin Algorithm page
@app.route('/round-robin', methods=['GET', 'POST'])
def round_robin():
    if request.method == 'POST':
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')
        time_quantum = request.form.get('time-quantum')

        return run_rr(arrival_times, burst_times, time_quantum)

    return render_template('round_robin.html')


def run_rr(arrival_times, burst_times, time_quantum):
    try:
        arrival_times = list(map(int, arrival_times.strip().split(' ')))
        burst_times = list(map(int, burst_times.strip().split(' ')))

        if time_quantum == '':
            time_quantum = 2
        else:
            time_quantum = int(time_quantum)

        n = len(arrival_times)
        processes = list(range(n))

        if n != len(burst_times):
            raise Exception("ERROR!!\n\nNumber of Arrival Time and Burst Time must be equal.")

        scheduler = Round_Robin()
        result = scheduler.round_robin(processes, arrival_times, burst_times, time_quantum)
        return result

    except Exception as error:
        result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
        return result


@app.route('/compare', methods=['GET', 'POST'])
def compare():
    global global_arrival_times
    global global_burst_times
    global global_time_quantum
    global global_priority
    global algo

    if request.method == 'POST':
        algo = request.form.get('algo')
        print('Algorithm accessed : ', algo)

        if algo is None:
            global_arrival_times = request.form.get('arrival-time')
            global_burst_times = request.form.get('burst-time')
            global_time_quantum = request.form.get('time-quantum')
            global_priority = request.form.get('priority')

        else:
            global_time_quantum = request.form.get('tQ')
            global_priority = request.form.get('priority')

            if algo == 'fcfs':
                return run_fcfs(global_arrival_times, global_burst_times)

            elif algo == 'sjfnp':
                return run_sjfnp(global_arrival_times, global_burst_times)

            if algo == 'sjfp':
                return run_sjfp(global_arrival_times, global_burst_times)

            elif algo == 'priority':
                return run_priority(global_arrival_times, global_burst_times, global_priority)

            elif algo == 'rr':
                return run_rr(global_arrival_times, global_burst_times, global_time_quantum)

    return render_template('compare.html', wt="--", tat="--")


# Route for returning to the main menu
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
