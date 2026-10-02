import time
import random
from itertools import combinations
import matplotlib.pyplot as plt

def baseline_solution(tasks):
    max_revenue = 0
    best_schedule = []

    for i in range(1, len(tasks) + 1):
        for subset in combinations(tasks, i):
            current_schedule = list(subset)
            current_schedule.sort()
            is_valid = True
            current_revenue = 0

            for day, (deadline, pay) in enumerate(current_schedule, start=1):
                if day > deadline:
                    is_valid = False
                    break
                current_revenue = current_revenue + pay

            if is_valid and current_revenue > max_revenue:
                max_revenue = current_revenue
                best_schedule = current_schedule

    return max_revenue, best_schedule


def freelanceTasksGreedy(tasks):
    if not tasks:
        return 0, []
    tasks = sorted(tasks, key=lambda x: x[1], reverse=True)
    max_deadline = max((deadline for deadline, _ in tasks))
    schedule = [None] * (max_deadline)
    revenue = 0
    for deadline, pay in tasks:
        for day in range(min(deadline - 1, max_deadline - 1), -1, -1):
            if schedule[day] is None:
                schedule[day] = (deadline, pay)
                revenue += pay
                break
    return revenue, schedule

client_tasks = [(2, 50), (1, 45), (2, 40), (1, 60), (3, 45), (3, 90), (4, 34), (5, 35), (3, 65), (5, 60), (1, 65), (2, 30)]
revenue, schedule = baseline_solution(client_tasks)

print(f"Max Revenue: ${revenue}")
print(f"Optimal Schedule: {schedule}")

tasks = [(2, 50), (1, 45), (2, 40), (1, 60), (3, 45), (3, 90), (4, 34), (5, 35), (3, 65), (5, 60), (1, 65), (2, 30)]
print(freelanceTasksGreedy(tasks))

def generate_mock_tasks(size):
    return [(random.randint(1, max(1, size // 2)), random.randint(10, 500)) for _ in range(size)]

def run_visual_benchmark():
    sizes = list(range(4, 20))
    baseline_times = []
    greedy_times = []
    
    for size in sizes:
        tasks_pool = generate_mock_tasks(size)
        
        # Benchmark Baseline
        start = time.perf_counter()
        baseline_solution(tasks_pool)
        baseline_times.append(time.perf_counter() - start)
        
        # Benchmark Greedy
        start = time.perf_counter()
        freelanceTasksGreedy(tasks_pool)
        greedy_times.append(time.perf_counter() - start)
        
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, baseline_times, label='Baseline: Brute Force $O(2^n)$', color='crimson', marker='o', linewidth=2)
    plt.plot(sizes, greedy_times, label='Proposed: Greedy $O(n \log n)$', color='dodgerblue', marker='s', linewidth=2)
    
    plt.title('Algorithm Empirical Performance Comparison', fontsize=14, fontweight='bold')
    plt.xlabel('Input Size (Number of Tasks, $N$)', fontsize=12)
    plt.ylabel('Execution Time (seconds, logarithmic scale)', fontsize=12)
    plt.yscale('log')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=11)
    plt.show()

if __name__ == "__main__":
    run_visual_benchmark()
