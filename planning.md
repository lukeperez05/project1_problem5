# Planning and Analysis

## Problem Formulation

The objective of this Freelance Task problem is to create a schedule using a given list of tuples that maximizes revenue. We are provided a list of tuples of size two denoted as Tasks = =[(Deadline1 , Pay1), (Deadline 2, Pay 2), …, (Deadline n, Pay n)]. The constraints of this problem is that only one task can be worked on at one time, and that task takes 1 day to complete. Each item in the list is designated as a tuple that has two elements: deadline corresponding to the day which the task must be completed by or it will be unable, and pay corresponding to the revenue that will be gained by completing the task. Our goal is to design an algorithm that both returns a schedule that has been specifically chosen because it produces the maximum amount of revenue with the deadlines, and returns the maximum revenue of that schedule when it is completed. 

## Baseline Solution

```text
from itertools import combinations

def freelance_tasks(tasks):
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

client_tasks = [(2, 50), (1, 45), (2, 40), (1, 60)]
revenue, schedule = freelance_tasks(client_tasks)

print(f"Max Revenue: ${revenue}")
print(f"Optimal Schedule: {schedule}")
```

## Algorithmic Strategy

To efficiently find the optimal schedule with the biggest payout, we use a greedy algorithm strategy that sorts through the ‘tasks’ list and pairs the biggest payout tuple with the closest it can get to the deadline as possible without going over. 

We begin by sorting the list of tuples by highest pay first (the second element in each tuple). We set a max_deadline that takes the maximum of the deadlines of the list (the first element in each tuple). We create a schedule list of nones that is multiplied by the maximum deadline + 1. This creates a list of nones that is equal to the amount of days that will be scheduled. We then create a revenue variable that will count how much the most profitable schedule will make. 

A for loop is created that iterates through the entire ‘tasks’ list from beginning to end. Inside we run another for loop that will find the minimum of the deadline –1 to the max deadline -1. This will make sure that the deadline that the task has does not go over the day that the algorithm is trying to fill. An if statement is placed to check if the proposed day where the tuple will reside is filled or not. If it is not filled, the tuple will be placed where the none would be and the pay will be added to the revenue. In the end, the for loop will iterate through the entire ‘tasks’ list making sure that each day in schedule is filled with the most profitable task. Lastly, returning the revenue and schedule list of tuples. 


```text
Algorithm freelanceTasksGreedy(tasks):
   input: list of tuples of size two with the two elements being ‘deadline’ and ‘pay’
   output: list of tuples of size two corresponding to the desired schedule and an int corresponding to maximum revenue
  
   Sort list ‘tasks’ by highest pay first
   max_deadline = max(deadline for deadline, _ in tasks)
   schedule = list of none * max_deadline + 1
   revenue = 0
   for deadline, pay in tasks:
       for day in range of the minimum of deadline - 1 to max_deadline to -1, going down by 1:
           if schedule[day] is None:
               schedule[day] = (deadline, pay)
               revenue += pay
               break
       return revenue, schedule
```

## Complexity Analysis

In our baseline solution, the outer loop generates 2^n - 1 combinations using the function - combinations(tasks, i). For each generated subset of size i, the dominant operations are the sorting step (current_schedule.sort()), which takes O(ilogi) time according to our variable i, and the validation loop, which takes O(i) time. Because the largest subsets approach size n and the total number of subsets is exponential, which means they use O(2^n), the upper bound is strictly limited by the largest combinations multiplied by their sorting which means the Big O bound is O(2^n). 