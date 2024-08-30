class SJF_Preemtive:
    def __init__(self):
        pass

    def findWaitingTime(self, processes, n, bt, wt, at):
        remaining_bt = bt[:]
        completed = 0
        current_time = 0
        min_bt = float('inf')
        shortest = 0
        finish_time = 0
        check = False
        execution_order = []

        # Initialize the waiting time
        wt[:] = [0] * n

        # Process until all processes are completed
        while completed != n:
            # Find process with the shortest remaining time at current_time
            for j in range(n):
                if (at[j] <= current_time and remaining_bt[j] < min_bt and remaining_bt[j] > 0):
                    min_bt = remaining_bt[j]
                    shortest = j
                    check = True

            if not check:
                current_time += 1
                continue

            # Record the execution order
            execution_order.append(shortest)

            # Reduce remaining time by one unit
            remaining_bt[shortest] -= 1

            # Update minimum
            min_bt = remaining_bt[shortest]
            if min_bt == 0:
                min_bt = float('inf')

            # If a process gets completely executed
            if remaining_bt[shortest] == 0:
                completed += 1
                check = False

                # Find the finish time of current process
                finish_time = current_time + 1

                # Calculate waiting time
                wt[shortest] = finish_time - bt[shortest] - at[shortest]

                if wt[shortest] < 0:
                    wt[shortest] = 0

            # Increment time
            current_time += 1

        return execution_order

    def findTurnAroundTime(self, n, bt, wt, tat):
        for i in range(n):
            tat[i] = bt[i] + wt[i]

    def findAverageTime(self, n, processes, bt, at):
        wt = [0] * n
        tat = [0] * n

        execution_order = self.findWaitingTime(processes, n, bt, wt, at)
        self.findTurnAroundTime(n, bt, wt, tat)

        total_wt = sum(wt)
        total_tat = sum(tat)

        result = "Process\tArrival_Time\tBurst_Time\tWaiting_Time\tTurnaround_Time\n"
        for i in range(n):
            result += f"{processes[i]}\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}\n"

        avg_wt = total_wt / n
        avg_tat = total_tat / n
        result+= f"\nAverage Waiting Time: {avg_wt:.2f}\n"
        result += f"Average Turnaround Time: {avg_tat:.2f}\n"
        
        result += '\n' + self.draw_gantt_chart(execution_order)
        
        return result

    def draw_gantt_chart(execution_order):
        gantt_chart = "|"
        prev_process = execution_order[0]

        for process in execution_order:
            if process != prev_process:
                gantt_chart += f"  P{prev_process + 1}  |"
                prev_process = process
            else:
                prev_process = process
                
        gantt_chart += '  P' + str(execution_order[len(execution_order) - 1] + 1) + "  |"

        top = '_' * len(gantt_chart)
        bottom = '‾' * len(gantt_chart)
        gantt_chart = 'Gantt Chart:\n' + top + '\n' + gantt_chart + '\n' + bottom

        return gantt_chart
        
        

    def main(self):
        n = int(input("Enter the number of processes: "))
        
        processes = list(range(n))
        burst_time = []
        arrival_time = []

        for i in range(n):
            at = int(input(f"Enter Arrival Time for Process {i}: "))
            bt = int(input(f"Enter Burst Time for Process {i}: "))
            arrival_time.append(at)
            burst_time.append(bt)

        self.findAverageTime(n, processes, burst_time, arrival_time)

if __name__ == "__main__":
    scheduler = SJF_Preemtive()
    scheduler.main()
