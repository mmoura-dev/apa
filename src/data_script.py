import csv
import os
from load_balancing_problem.task import Task


def get_file_size_mb(file_name) -> float:
    return os.path.getsize(file_name) / (1024 ** 2)

def generate_uniform_tasks(num_tasks, id_offset=0):
    return [Task(i, 1) for i in range(id_offset + 1, num_tasks + id_offset + 1)]

def task_to_tuple(task: Task):
    return task.id, task.length, "very-long-filler"*200

def write_large_task_file(filename, target_size_mb, gen_tasks_func):
    """Write a file with serialized Task instances until it reaches the target size."""
    buffer_size = 10000

    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        i = 0
        while get_file_size_mb(filename) < target_size_mb:
            writer.writerows([task_to_tuple(t) for t in gen_tasks_func(buffer_size, buffer_size * i)])
            csv_file.flush()
            i += 1
    print("%.2f MB" %(get_file_size_mb(filename)))


if __name__ == "__main__":
    target_size_mb = 300
    filename_template = "./data/%s.csv"
    write_large_task_file(filename_template %"constant_tasks", target_size_mb, generate_uniform_tasks)
