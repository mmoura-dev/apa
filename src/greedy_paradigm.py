import csv
from dataclasses import dataclass
from typing import Iterable, Sequence
from load_balancing_problem import Task, VirtualMachine


@dataclass
class VMIndex:
    mips: int
    etc: float = 0.0


def get_tasks_generator(file_name: str) -> Iterable[Task]:
    with open("./data/%s" % file_name, "r") as file:
        reader = csv.reader(file)
        for id, length, _ in reader:
            yield Task(int(id), int(length))


def get_greedy_solution_makespan(
    tasks: Iterable[Task], vms: Sequence[VirtualMachine]
) -> int:
    vms_index = [VMIndex(vm.processing_power) for vm in vms]
    # print("vms_index: ", vms_index)

    for task in tasks:
        # print("task: ", task)
        min_etc = min(vms_index, key = lambda vmi: vmi.etc).etc
        # print("min_etc: ", min_etc)
        vmis_with_min_etc = filter(lambda vmi: vmi.etc <= min_etc, vms_index)
        # print("vmis_with_min_etc: ", vmis_with_min_etc)
        chosen_vmi = min(vmis_with_min_etc, key = lambda vmi: vmi.mips)
        # print("chosen_vmi: ", chosen_vmi)
        chosen_vmi.etc += task.length / chosen_vmi.mips
        # print("chosen_vmi.etc: ", chosen_vmi.etc)
        # print("vms_index: ", vms_index)

    return max(vms_index, key = lambda vmi: vmi.etc).etc


if __name__ == "__main__":
    DATA_FILE = "constant_tasks.csv"
    tasks_generator = get_tasks_generator(DATA_FILE)

    # task_list = [Task(1, 1), Task(2, 1), Task(3, 2), Task(4, 1), Task(5, 1), Task(6, 2)]
    vm_list = [VirtualMachine(1), VirtualMachine(2), VirtualMachine(1)]

    solution = get_greedy_solution_makespan(tasks_generator, vm_list)
    print("Expected time to compute: ", solution)
