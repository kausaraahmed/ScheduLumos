class Priority_Scheduling():
    def __init__(self):
        pass
        
    def priority_scheduling(self, processes, arrival_time, burst_time, priority):
        n = len(processes)
        waiting_time = [0] * n
        turnaround_time = [0] * n
        completion_time = [0] * n
        execution_order = []

        # Sorting processes based on priority
        combined = list(zip(processes, arrival_time, burst_time, priority))
        combined.sort(key=lambda x: x[3])  # Sort by priority
        sorted_processes, sorted_arrival_time, sorted_burst_time, sorted_priority = zip(*combined)

        # Calculating waiting time and turnaround time
        waiting_time[0] = 0
        completion_time[0] = sorted_burst_time[0]
        turnaround_time[0] = completion_time[0]
        execution_order.append(sorted_processes[0])

        for i in range(1, n):
            waiting_time[i] = completion_time[i-1] - sorted_arrival_time[i]
            if waiting_time[i] < 0:
                waiting_time[i] = 0
            completion_time[i] = waiting_time[i] + sorted_burst_time[i] + sorted_arrival_time[i]
            turnaround_time[i] = completion_time[i] - sorted_arrival_time[i]
            waiting_time[i] = turnaround_time[i] - sorted_burst_time[i]
            execution_order.append(sorted_processes[i])

        avg_waiting_time = sum(waiting_time) / n
        avg_turnaround_time = sum(turnaround_time) / n

        result = 'Process_no\tArrival_Time\tBurst_Time\tCompletion_Time\tTurnAround_Time\tWaiting_Time\n'
        for i in range(n):
            result += f"{sorted_processes[i]+1}\t\t{sorted_arrival_time[i]}\t\t{sorted_burst_time[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}\n"
        
        result += f"\nAverage Waiting Time: {avg_waiting_time:.2f}\n"
        result += f"Average Turnaround Time: {avg_turnaround_time:.2f}\n"
        
        result += '\n' + self.draw_gantt_chart(execution_order)
        
        return result

    def draw_gantt_chart(self, execution_order):
        gantt_chart = "|"
        prev_process = execution_order[0]

        for process in execution_order:
            if process != prev_process:
                gantt_chart += f"  P{prev_process + 1}  |"
                prev_process = process
            else:
                prev_process = process
                
        gantt_chart += '  P' + str(execution_order[-1] + 1) + "  |"

        top = '_' * len(gantt_chart)
        bottom = '‾' * len(gantt_chart)
        gantt_chart = 'Gantt Chart:\n' + top + '\n' + gantt_chart + '\n' + bottom

        return gantt_chart

    def main(self):
        num_processes = int(input("Enter the number of processes: "))
        
        processes = list(range(num_processes))
        arrival_time = list(map(int, input("Enter the arrival time of the processes: ").split()))
        burst_time = list(map(int, input("Enter the burst time of the processes: ").split()))
        priority = list(map(int, input("Enter the priority of the processes: ").split()))
        
        print(self.priority_scheduling(processes, arrival_time, burst_time, priority))

if __name__ == "__main__":
    scheduler = Priority_Scheduling()
    scheduler.main()

