from functools import reduce
import math
from typing import Callable
import numpy as np
import itertools

tasks_set = np.arange(1, 7)
get_task_length = lambda x: 1 if x != 0 else 0
vms_set = np.arange(1, 4)
get_vm_processing_power = lambda x: 1


# TODO: These are not all possible solutions. Solutions with unbalanced distribution of tasks per vm are missing.
def get_all_possible_solutions(
    tasks_set: np.ndarray, vms_set: np.ndarray
) -> np.ndarray:
    number_of_tasks = len(tasks_set)
    number_of_columns = len(vms_set)
    number_of_rows = math.ceil(number_of_tasks / number_of_columns)
    task_permutations = [
        np.array(tp) for tp in itertools.permutations(tasks_set, number_of_tasks)
    ]

    if number_of_tasks % number_of_columns != 0:
        padding = (number_of_rows * number_of_columns) - number_of_tasks
        task_permutations = [
            np.pad(tp, (0, padding), mode="constant") for tp in task_permutations
        ]

    return [tp.reshape(number_of_rows, number_of_columns) for tp in task_permutations]


def get_column_cost(col: np.ndarray, get_task_size: Callable[[int], int]) -> int:
    return reduce(lambda acc, x: acc + get_task_size(x), col, 0)


def cost_function(
    solution_matrix: np.ndarray,
    get_vm_pp: Callable[[int], int],
    get_task_size: Callable[[int], int],
) -> int:
    max_cost = -math.inf
    for column_index in range(1, len(solution_matrix)):
        column_etc = get_column_cost(
            solution_matrix[column_index], get_task_size
        ) / get_vm_pp(column_index)
        if column_etc > max_cost:
            max_cost = column_etc
    return max_cost


def brute_force(
    tasks: np.ndarray,
    vms: np.ndarray,
    task_length_function: Callable[[int], int],
    vm_processing_power_function: Callable[[int], int],
) -> np.ndarray:
    best_solution = None
    best_solution_cost = math.inf
    possible_solutions = get_all_possible_solutions(tasks, vms)

    for solution in possible_solutions:
        solution_cost = cost_function(
            solution, task_length_function, vm_processing_power_function
        )
        if solution_cost < best_solution_cost:
            best_solution = solution
            best_solution_cost = solution_cost

    return best_solution, best_solution_cost


print(brute_force(tasks_set, vms_set, get_task_length, get_vm_processing_power))
