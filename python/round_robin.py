from python.utils import Utils


class RoundRobin:
    def __init__(self):
        pass

    def round_robin(self, processes, arrival_time, burst_time, time_quantum):
        n = len(processes)
        remaining_burst_time = burst_time[:]
        waiting_time = [0] * n
        turnaround_time = [0] * n
        completion_time = [0] * n
        t = 0
        queue = []
        current_time = 0
        completed = 0
        marked = [False] * n
        execution_order = []

        while completed != n:
            for i in range(n):
                if arrival_time[i] <= current_time and not marked[i]:
                    queue.append(i)
                    marked[i] = True

            if not queue:
                current_time += 1
                continue

            idx = queue.pop(0)
            execution_order.append(idx)

            if remaining_burst_time[idx] > time_quantum:
                remaining_burst_time[idx] -= time_quantum
                current_time += time_quantum
                for i in range(n):
                    if arrival_time[i] <= current_time and not marked[i]:
                        queue.append(i)
                        marked[i] = True
                queue.append(idx)
            else:
                current_time += remaining_burst_time[idx]
                completion_time[idx] = current_time
                waiting_time[idx] = current_time - burst_time[idx] - arrival_time[idx]
                turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
                remaining_burst_time[idx] = 0
                completed += 1

        avg_waiting_time = sum(waiting_time) / n
        avg_turnaround_time = sum(turnaround_time) / n

        result = "Program No.\tArrival Time\tBurst Time\tWait Time\tTurnAround Time\n"
        for i in range(n):
            result += f"{i + 1}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\n"

        result += f"\nAverage Waiting Time: {avg_waiting_time:.2f}\n"
        result += f"Average Turnaround Time: {avg_turnaround_time:.2f}\n"

        result += '\n' + Utils().draw_gantt_chart(execution_order)

        return result