from functools import reduce
import math
from typing import Iterable, List, Optional, Sequence

from .task import Task
from .virtual_machine import VirtualMachine


class LoadBalancingProblem:
    def __init__(self, task_list: List[Task], vm_list: List[VirtualMachine]) -> None:
        self.task_list = task_list
        self.vm_list = vm_list

    def sum_tasks_length(self, tasks: Iterable[Optional[Task]]) -> int:
        return reduce(lambda acc, x: acc + x.length if x is not None else acc, tasks, 0)

    def calculate_makespan(
        self, solution_matrix: Sequence[Sequence[Optional[Task]]]
    ) -> float:
        # return max([self.sum_tasks_length(task_list) / vm.processing_power for task_list, vm in zip(solution_matrix, self._vm_list)])
        max_cost = -math.inf
        for task_list, vm in zip(solution_matrix, self.vm_list):
            length_sum = self.sum_tasks_length(task_list)
            task_list_etc = length_sum / vm.processing_power
            if task_list_etc > max_cost:
                max_cost = task_list_etc
        return max_cost
