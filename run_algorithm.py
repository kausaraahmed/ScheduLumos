from fcfs import FCFS
from SJF_nonPreemptive import SJF_nonPreemtive
from SJF_Preemptive import SJF_Preemtive
from priority_scheduling import Priority_Scheduling
from round_robin import Round_Robin

class Run_Algorithm():
    def __init__(self):
        pass
    
    def run_fcfs(self, arrival_times, burst_times):
        try:
            arrival_times = list(map(int, arrival_times.strip().split(' ')))
            burst_times = list(map(int, burst_times.strip().split(' ')))
            n = len(arrival_times)
            processes = list(range(n))

            if n != len(burst_times):
                raise Exception("Number of Arrival Time and Burst Time must be equal.")
            
            self.input_validation(arrival_times)
            self. input_validation(burst_times)

            return FCFS().find_average_time(processes, n, burst_times, arrival_times)

        except Exception as error:
            result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
            return result
        
        
    def run_sjfnp(self, arrival_times, burst_times):
        try:
            arrival_times = list(map(int, arrival_times.strip().split(' ')))
            burst_times = list(map(int, burst_times.strip().split(' ')))
            n = len(arrival_times)
            processes = list(range(n))

            if n != len(burst_times):
                raise Exception("Number of Arrival Time and Burst Time must be equal.")

            self.input_validation(arrival_times)
            self.input_validation(burst_times)
            
            return SJF_nonPreemtive().findAverageTime(n, processes, burst_times, arrival_times)

        except Exception as error:
            result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
            return result
        
        
    def run_sjfp(self, arrival_times, burst_times):
        try:
            arrival_times = list(map(int, arrival_times.strip().split(' ')))
            burst_times = list(map(int, burst_times.strip().split(' ')))
            n = len(arrival_times)
            processes = list(range(n))

            if n != len(burst_times):
                raise Exception("Number of Arrival Time and Burst Time must be equal.")

            self.input_validation(arrival_times)
            self.input_validation(burst_times)
            
            return SJF_Preemtive().findAverageTime(n, processes, burst_times, arrival_times)

        except Exception as error:
            result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
            return result
        
        
    def run_priority(self, arrival_times, burst_times, priority):
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

            self.input_validation(arrival_times)
            self.input_validation(burst_times)
            self.input_validation(priority)

            return Priority_Scheduling().priority_scheduling(processes, arrival_times, burst_times, priority)

        except Exception as error:
            result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
            return result
        
    def run_rr(self, arrival_times, burst_times, time_quantum):
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
            elif time_quantum < 1:
                raise Exception("ERROR!!\n\nTime Quantum must be greater than 0.")

            return Round_Robin().round_robin(processes, arrival_times, burst_times, time_quantum)

        except Exception as error:
            result = "An ERROR occurred: \n\n" + str(type(error).__name__) + " - " + str(error)
            return result
        
    def input_validation(self, times):
        for i in times:
            if i < 0:
                raise Exception("All Arrival Times and Burst Times must be positive.")
