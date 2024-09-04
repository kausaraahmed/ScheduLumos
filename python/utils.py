def draw_gantt_chart(exe_order):
    gantt_chart = '|'
    for _ in exe_order:
        gantt_chart += "  P" + str(_ + 1) + "  |"

    top = '_' * len(gantt_chart)
    bottom = '‾' * len(gantt_chart)
    gantt_chart = 'Gantt Chart:\n' + top + '\n' + gantt_chart + '\n' + bottom

    return gantt_chart


def splitter(string):
    return list(map(int, string.strip().split(' ')))


def input_validation(times):
    for i in times:
        if i < 0:
            raise Exception("All Arrival Times and Burst Times must be positive.")
