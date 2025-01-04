import itertools
import math
from pprint import pprint
from typing import Iterable, Sequence
import numpy as np
from load_balancing_problem import Task
from load_balancing_problem import VirtualMachine
from load_balancing_problem import LoadBalancingProblem


def get_all_possible_solutions(
    lb_problem: LoadBalancingProblem,
) -> Iterable[Sequence[Sequence[Task]]]:

    number_of_tasks = len(lb_problem.task_list)
    number_of_columns = len(lb_problem.vm_list)
    number_of_rows = math.ceil(number_of_tasks / number_of_columns)

    task_permutations = [
        np.array(permut)
        for permut in itertools.permutations(lb_problem.task_list, number_of_tasks)
    ]

    if number_of_tasks % number_of_columns != 0:
        padding = (number_of_rows * number_of_columns) - number_of_tasks
        task_permutations = [
            np.pad(tp, (0, padding), constant_values=None) for tp in task_permutations
        ]

    return [tp.reshape(number_of_columns, number_of_rows) for tp in task_permutations]


if __name__ == "__main__":
    problem = LoadBalancingProblem(
        task_list=[Task(1, 1), Task(2, 1), Task(3, 2), Task(4, 1), Task(5, 1), Task(6, 2)],
        vm_list=[VirtualMachine(1), VirtualMachine(2), VirtualMachine(1)],
    )

    possible_solutions = get_all_possible_solutions(problem)
    minimum_makespan_solution = min(
        [
            (problem.calculate_makespan(solution), solution)
            for solution in possible_solutions
        ],
        key=lambda x: x[0],
    )
    pprint(minimum_makespan_solution)
