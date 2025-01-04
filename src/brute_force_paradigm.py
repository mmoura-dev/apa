import itertools
import math
import sys
from typing import Iterable, Sequence

import numpy as np
from load_balancing_problem import LoadBalancingProblem, Task, VirtualMachine
from tasks_from_file import get_tasks_generator


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


def get_brute_force_solution_makespan(
    tasks: Iterable[Task], vms: Sequence[VirtualMachine]
) -> int:
    STEP = 5
    cummulative_etc = 0
    processed_tasks = 0

    while True:
        buffer = []
        buffer.extend(itertools.islice(tasks, STEP))
        lb_problem = LoadBalancingProblem(buffer, vms)

        print(buffer)
        possible_solutions = get_all_possible_solutions(lb_problem)
        print(len(possible_solutions))
        minimum_makespan_solution = min(
            [
                (lb_problem.calculate_makespan(solution), solution)
                for solution in possible_solutions
            ],
            key=lambda x: x[0],
        )

        cummulative_etc += minimum_makespan_solution[0]
        print("Accumulated etc: ", cummulative_etc)
        processed_tasks += len(buffer)
        if len(buffer) < STEP:
            break
    return cummulative_etc


if __name__ == "__main__":
    tasks_generator = get_tasks_generator(sys.argv[1] if len(sys.argv) > 1 else "uniform_tasks.csv")
    task_list = [Task(1, 1), Task(2, 1), Task(3, 2), Task(4, 1), Task(5, 1), Task(6, 2)]
    vm_list = [VirtualMachine(1), VirtualMachine(2), VirtualMachine(1)]

    solution_etc = get_brute_force_solution_makespan(tasks_generator, vm_list)
    print("Expected time to compute (etc): ", solution_etc)
