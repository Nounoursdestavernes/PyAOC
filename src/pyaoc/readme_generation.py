# This file contains functions to generate the README.md
import os
from jinja2 import Environment, PackageLoader
from pyaoc.check_day import check_name_folder, check_day_structure
from pyaoc.check_parameters import check_year_number
from pyaoc.day_subject import get_day_name

#Jinja2 environment
env = Environment(
    loader=PackageLoader('pyaoc', '.'),
)


def generate_readme(year_number: int = 2023) -> None:
    """Generate the README

    Returns None if the generation is successful, else sys.exit.
    
    :param int year_number: Number of the year. Must be between 2015 and current year

    :return: None
    :rtype: None
    """

    check_year_number(year_number) # Check if year_number is valid

    todo_days = []
    files = os.listdir()
    for file in files:
        if os.path.isdir(file) and len(file) == 5 and file[:3] == 'day' and file[3:].isdigit() and 1 <= int(file[3:]) <= 25:
            todo_days.append(file)
    
    days = []
    for day in todo_days:
        number = int(day[3:])
        check_day_structure(number)
        name = get_day_name(number, year_number)
        benchmark = open(os.path.join(day, "benchmark", "benchmark.txt"), "r").read()
        if len(benchmark) == 0:
            benchmark = "Not benchmarked\n"
        days.append((day[3:], name, benchmark))

    days.sort()

    template = env.get_template("README.jinja2")

    with open("README.md", "w") as f:
        f.write(template.render(days = days, year=year_number))

    return None





