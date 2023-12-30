# This file contains functions to generate the README.md
import os
from jinja2 import Environment, PackageLoader
from pyaoc.day_subject import get_day_name

#Jinja2 environment
env = Environment(
    loader=PackageLoader('pyaoc', '.'),
)

def correct_name_folder(name: str) -> bool:
    """Check that the folder have a name in following format : day{day_number}

    Where {day_number} is a number between 01 and 25.

    :param int name: Name of the folder.

    :return: valide
    :rtype: bool
    """
    if len(name) != 5:
        return False
    
    day_number = name[3:]
    if name[:3] != 'day' and not day_number.isdigit():
        return False
    
    day_number = int(day_number)

    if day_number < 1 or day_number > 25:
        return False
    
    return True


def generate_readme(year: int = 2023) -> int:
    """Generate the README

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param int part_number: Number of the part. Corresponding file must exist.
    :param int year_number: Number of the year. Must be between 2015 and current year

    :return: error
    :rtype: int
    """
    days = []
    files = os.listdir()
    for file in files:
        if os.path.isdir(file) and correct_name_folder(file):
            days.append(file)
    
    data = []
    for day in days:
        number = int(day[3:])
        name = get_day_name(number, year)
        benchmark = open(os.path.join(day, "benchmark", "benchmark.txt"), "r").read()
        if len(benchmark) == 0:
            benchmark = "Not benchmarked\n"
        data.append((day[3:], name, benchmark))

    template = env.get_template("README.jinja2")

    data.sort()

    with open("README.md", "w") as f:
        f.write(template.render(days = data, year=year))

    return 0





