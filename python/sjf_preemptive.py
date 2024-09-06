from python.utils import Utils


class SjfPreemptive:
    def __init__(self):
        pass

    def find_waiting_time(self, processes, n, bt, wt, at):
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
                if at[j] <= current_time and min_bt > remaining_bt[j] > 0:
                # if at[j] <= current_time and remaining_bt[j] < min_bt and remaining_bt[j] > 0:
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

    def find_turn_around_time(self, n, bt, wt, tat):
        for i in range(n):
            tat[i] = bt[i] + wt[i]

    def find_average_time(self, n, processes, bt, at):
        wt = [0] * n
        tat = [0] * n

        execution_order = self.find_waiting_time(processes, n, bt, wt, at)
        self.find_turn_around_time(n, bt, wt, tat)

        total_wt = sum(wt)
        total_tat = sum(tat)

        result = "Process\tArrival_Time\tBurst_Time\tWaiting_Time\tTurnaround_Time\n"
        for i in range(n):
            result += f"{processes[i]}\t{at[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}\n"

        avg_wt = total_wt / n
        avg_tat = total_tat / n
        result += f"\nAverage Waiting Time: {avg_wt:.2f}\n"
        result += f"Average Turnaround Time: {avg_tat:.2f}\n"

        result += '\n' + Utils().draw_gantt_chart(execution_order)

        return result

    def main(self):
        n = int(input("Enter the number of processes: "))
        processes = list(range(n))
        burst_time = []
        arrival_time = []

        self.find_average_time(n, processes, burst_time, arrival_time)


if __name__ == "__main__":
    scheduler = SjfPreemptive()
    scheduler.main()
