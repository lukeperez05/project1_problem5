from itertools import combinations

def baseline_solution(tasks):
    max_revenue = 0
    best_schedule = []

    for i in range(1, len(tasks) + 1):
        for subset in combinations(tasks, i):
        # Takes all combinations of the tasks from the input list and makes each a subset

            current_schedule = list(subset)
            # convert the subsets of combinations to lists
            current_schedule.sort()
            # sort them to check for deadlines easier
            is_valid = True
            current_revenue = 0

            for day, (deadline, pay) in enumerate(current_schedule, start=1):
                if day > deadline:
                    is_valid = False
                    break
                    # because the deadline was missed
                current_revenue = current_revenue + pay

            if is_valid and current_revenue > max_revenue:
                max_revenue = current_revenue
                best_schedule = current_schedule

    return max_revenue, best_schedule

client_tasks = [(2, 50), (1, 45), (2, 40), (1, 60), (3, 45), (3, 90), (4, 34), (5, 35), (3, 65), (5, 60), (1, 65), (2, 30)]
revenue, schedule = baseline_solution(client_tasks)

print(f"Max Revenue: ${revenue}")
print(f"Optimal Schedule: {schedule}")

def freelanceTasksGreedy(tasks):
    tasks = sorted(tasks, key=lambda x: x[1], reverse = True)
    max_deadline = max((deadline for deadline, _ in tasks))
    schedule = [None] * (max_deadline)
    revenue = 0
    for deadline, pay in tasks:
        for day in range(min(deadline - 1, max_deadline), -1, -1):
            if schedule[day] is None:
                schedule[day] = (deadline, pay)
                revenue += pay
                break
    return revenue, schedule

tasks = [(2, 50), (1, 45), (2, 40), (1, 60), (3, 45), (3, 90), (4, 34), (5, 35), (3, 65), (5, 60), (1, 65), (2, 30)]
print(freelanceTasksGreedy(tasks))

