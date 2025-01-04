from dataclasses import dataclass
import sys
from typing import Iterable, Sequence
from load_balancing_problem import Task, VirtualMachine
from tasks_from_file import get_tasks_generator


@dataclass
class VMIndex:
    mips: int
    etc: float = 0.0


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
    tasks_generator = get_tasks_generator(sys.argv[1] if len(sys.argv) > 1 else "constant_tasks.csv")
    vm_list = [VirtualMachine(1), VirtualMachine(2), VirtualMachine(1)]

    solution_etc = get_greedy_solution_makespan(tasks_generator, vm_list)
    print("Expected time to compute: ", solution_etc)
