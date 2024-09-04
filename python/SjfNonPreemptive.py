class SjfNonPreemptive:
    def __init__(self):
        pass

    def findWaitingTime(self, processes, n, bt, wt, at):
        remaining_bt = bt[:]
        completed = 0
        current_time = 0
        execution_order = []

        while completed != n:
            shortest_index = -1
            shortest_bt = float('inf')

            for i in range(n):
                if at[i] <= current_time and shortest_bt > remaining_bt[i] > 0:
                    shortest_bt = remaining_bt[i]
                    shortest_index = i

            if shortest_index == -1:
                current_time += 1
                continue

            current_time += bt[shortest_index]
            remaining_bt[shortest_index] = 0
            wt[shortest_index] = current_time - bt[shortest_index] - at[shortest_index]
            execution_order.append(shortest_index)

            if wt[shortest_index] < 0:
                wt[shortest_index] = 0

            completed += 1
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
            result += f"{i + 1}\t\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}\n"

        result += f"\nAverage Waiting Time: {total_wt / n:.2f}\n"
        result += f"Average Turnaround Time: {total_tat / n:.2f}\n"

        result += '\n' + self.draw_gantt_chart(execution_order)

        return result  # Return the result string

    def draw_gantt_chart(self, exe_order):
        gantt_chart = '|'
        for _ in exe_order:
            gantt_chart += "  P" + str(_ + 1) + "  |"

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
    scheduler = SjfNonPreemptive()
    scheduler.main()
