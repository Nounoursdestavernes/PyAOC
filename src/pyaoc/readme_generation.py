# This file contains functions to generate the README.md
import logging
import os
from jinja2 import Environment, PackageLoader
from pyaoc.check_day import check_name_folder, check_day_structure
from pyaoc.day_subject import get_day_name

#Jinja2 environment
env = Environment(
    loader=PackageLoader('pyaoc', '.'),
)

logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')

def generate_readme(year_number: int = 2023) -> int:
    """Generate the README

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param int year_number: Number of the year. Must be between 2015 and current year

    :return: error
    :rtype: int
    """


    if type(year_number) != int:
        logging.error("Invalid year number : year_number must be an int")
        return 1

    if year_number < 2015:
        logging.error("year_number must be between 2015 and current year")
        return 1

    todo_days = []
    files = os.listdir()
    for file in files:
        if os.path.isdir(file) and check_name_folder(file):
            todo_days.append(file)
    
    days = []
    for day in todo_days:
        number = int(day[3:])
        if not check_day_structure(number):
            return 1
        
        name = get_day_name(number, year_number)
        benchmark = open(os.path.join(day, "benchmark", "benchmark.txt"), "r").read()
        if len(benchmark) == 0:
            benchmark = "Not benchmarked\n"
        days.append((day[3:], name, benchmark))

    days.sort()

    template = env.get_template("README.jinja2")


    with open("README.md", "w") as f:
        f.write(template.render(days = days, year=year_number))

    return 0





