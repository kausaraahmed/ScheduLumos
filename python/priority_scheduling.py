from python.utils import Utils


class PriorityScheduling:
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
            waiting_time[i] = completion_time[i - 1] - sorted_arrival_time[i]
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
            result += f"{sorted_processes[i] + 1}\t\t{sorted_arrival_time[i]}\t\t{sorted_burst_time[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}\n"

        result += f"\nAverage Waiting Time: {avg_waiting_time:.2f}\n"
        result += f"Average Turnaround Time: {avg_turnaround_time:.2f}\n"

        result += '\n' + Utils().draw_gantt_chart(execution_order)

        return result