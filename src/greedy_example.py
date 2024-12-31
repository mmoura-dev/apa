import math
from pprint import pprint
from typing import Sequence
from load_balancing_problem import Task
from load_balancing_problem import VirtualMachine
from load_balancing_problem import LoadBalancingProblem


def min_etc_columns(problem: LoadBalancingProblem, solution: Sequence[Sequence[Task]]) -> Sequence[int]:
    result = []
    min_etc = math.inf
    index = 0

    for column in solution:
        column_etc = problem.sum_tasks_length(column) / problem.vm_list[index].processing_power

        if column_etc == min_etc:
            result.append(index)

        elif column_etc < min_etc:
            result = [index]
            min_etc = column_etc

        index += 1
    
    return result


def min_min_greedy_algorithm(
    lb_problem: LoadBalancingProblem,
) -> Sequence[Sequence[Task]]:
    """Finds a solution for the load balancing problem using the min-min algorithm.

    The min-min algorithm works by matching the task with minimum length in the pool
    with the minimum processing power vm available.
    """
    solution = [[] for _ in range(len(lb_problem.vm_list))]
    length_sorted_tasks = sorted(lb_problem.task_list, key=lambda x: x.length)

    for task in length_sorted_tasks:
        available_vm_indexes = min_etc_columns(lb_problem, solution)
        chosen_vm_index = min(available_vm_indexes, key=lambda x: lb_problem.vm_list[x].processing_power)
        solution[chosen_vm_index].append(task)
        # pprint(solution)
        # print()

    return solution


if __name__ == "__main__":
    problem = LoadBalancingProblem(
        task_list=[
            Task(1, 1),
            Task(2, 1),
            Task(3, 2),
            Task(4, 1),
            Task(5, 1),
            Task(6, 2),
        ],
        vm_list=[VirtualMachine(1), VirtualMachine(2), VirtualMachine(1)],
    )

    min_min_solution = min_min_greedy_algorithm(problem)
    pprint((problem.calculate_makespan(min_min_solution), min_min_solution))
