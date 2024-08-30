from flask import Flask, render_template, request
from fcfs import FCFS
from  SJF_nonPreemptive import SJF_nonPreemtive
from  SJF_Preemptive import SJF_Preemtive
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
        # Get input values from the form
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')
        
        try:
            # Convert inputs to lists
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

    # Render the form on GET request
    return render_template('fcfs.html')

# Route for the SJF Non-Preemptive Algorithm page
@app.route('/sjf-non-preemptive', methods=['GET', 'POST'])
def sjf_non_preemptive():
    if request.method == 'POST':
        # Get input values from the form
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')
        
        try:
            # Convert inputs to lists
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

    # Render the form on GET request
    return render_template('sjf_non_preemptive.html')


# Route for the SJF Preemptive Algorithm page
@app.route('/sjf-preemptive', methods=['GET', 'POST'])
def sjf_preemptive():
    if request.method == 'POST':
        # Get input values from the form
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')
        
        try:
            # Convert inputs to lists
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

    # Render the form on GET request
    return render_template('sjf_preemptive.html')


# Route for the Priority Scheduling Algorithm page
@app.route('/priority-scheduling', methods=['GET', 'POST'])
def priority_scheduling():
    if request.method == 'POST':
        # Get input values from the form
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')
        priority = request.form.get('priority')
        
        try:
            # Convert inputs to lists
            arrival_times = list(map(int, arrival_times.strip().split(' ')))
            burst_times = list(map(int, burst_times.strip().split(' ')))
            priority = list(map(int, priority.strip().split(' ')))
            n = len(arrival_times)
            processes = list(range(n))
            
            if not (n == len(burst_times) == len(priority)):
                raise Exception("Number of Arrival Time, Burst Time and Priority must be equal.")
        
            scheduler = Priority_Scheduling()
            result = scheduler.priority_scheduling(processes, arrival_times, burst_times, priority)
            return result
        
        except Exception as error:
            result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
            return result 

    # Render the form on GET request
    return render_template('priority_scheduling.html')


# Route for the Round Robin Algorithm page
@app.route('/round-robin', methods=['GET', 'POST'])
def round_robin():
    if request.method == 'POST':
        # Get input values from the form
        arrival_times = request.form.get('arrival-time')
        burst_times = request.form.get('burst-time')
        time_quantam = request.form.get('time-quantam')  # Adjusted to match the form field name
        
        try:
            # Convert inputs to lists
            arrival_times = list(map(int, arrival_times.strip().split(' ')))
            burst_times = list(map(int, burst_times.strip().split(' ')))
            time_quantam = int(time_quantam)
            n = len(arrival_times)
            processes = list(range(n))
            
            if n != len(burst_times):
                raise Exception("ERROR!!\n\nNumber of Arrival Time and Burst Time must be equal.")
        
            scheduler = Round_Robin()
            result = scheduler.round_robin(processes, arrival_times, burst_times, time_quantam)
            return result
        
        except Exception as error:
            result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
            return result 

    # Render the form on GET request
    return render_template('round_robin.html')


# Route for returning to the main menu
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
