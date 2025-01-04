import csv
from typing import Iterable
from load_balancing_problem import Task


def get_tasks_generator(file_name: str) -> Iterable[Task]:
    with open("./data/%s" % file_name, "r") as file:
        reader = csv.reader(file)
        for id, length, _ in reader:
            yield Task(int(id), int(length))
