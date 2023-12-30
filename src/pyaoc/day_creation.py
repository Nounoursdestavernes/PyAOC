# This file contains functions to create a new day for Advent of Code
import logging
import os
import shutil
from jinja2 import Environment, PackageLoader

#Jinja2 environment
env = Environment(
    loader=PackageLoader('pyaoc', '.'),
)

# Logger
logger = logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')

def create_day(day_number: int = 1) -> int:
    """Create a new directory for a new day of Advent of Code.

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error
    
    :param int day_number: Number of the day. Must be between 1 and 25.

    :return: error
    :rtype: int
    """
    # Check if the day number is valid
    if day_number < 1 or day_number > 25:
        logging.error("Invalid day number : CREATE_DAY must be between 1 and 25")
        return 1
    
    # Create the directory
    dir_name = f"day{day_number:02d}"


    # Create folders
    if os.path.exists(dir_name):
        logging.error(f"Directory {dir_name} already exists")
        return 1
    
    os.mkdir(dir_name)
    os.chdir(dir_name)

    # Input folder
    if os.path.exists("inputs"):
        logging.error("inputs folder already exists")
        return 1
    
    os.mkdir("inputs")

    # Benchmark folder
    if os.path.exists("benchmark"):
        logging.error("benchmark folder already exists")
        return 1
    
    os.mkdir("benchmark")

    # Create files

    template = env.get_template("part.jinja2")


    # input and sample files
    os.chdir("inputs")
    with open("input.txt", "w") as f:
        pass
    with open("sample.txt", "w") as f:
        pass
    os.chdir("..")

    # part1 file
    with open("part1.py", "w") as f:
        f.write(template.render(day_number=day_number, part_number="1"))

    # part2 file
    with open("part2.py", "w") as f:
        f.write(template.render(day_number=day_number, part_number="2"))

    # return to the root directory
    os.chdir("..")

    return 0



def create_day_force(day_number: int = 1) -> int:
    """Create a new directory for a new day of Advent of Code. If the directory already exists, delete it and create a new one.
    
    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error
    
    :param int day_number: Number of the day. Must be between 1 and 25.

    :return: error
    :rtype: int
    """
    # Check if the day number is valid
    if day_number < 1 or day_number > 25:
        logging.error("Invalid day number : CREATE_DAY must be between 1 and 25")
        return 1
    
    # Create the directory
    dir_name = f"day{day_number:02d}"

    # Check if the directory already exists
    if os.path.exists(dir_name):
        # Delete the directory
        shutil.rmtree(dir_name)
    
    # Create folders

    os.mkdir(dir_name)
    os.chdir(dir_name)

    # Input folder
    if os.path.exists("inputs"):
        shutil.rmtree("inputs")
    os.mkdir("inputs")

    # Benchmark folder
    if os.path.exists("benchmark"):
        shutil.rmtree("benchmark")
    os.mkdir("benchmark")


    # Create files

    template = env.get_template("part.jinja2")

    # input and sample files
    os.chdir("inputs")
    with open("input.txt", "w") as f:
        pass
    with open("sample.txt", "w") as f:
        pass
    os.chdir("..")

    # part1 file
    with open("part1.py", "w") as f:
        f.write(template.render(day_number=day_number, part_number="1"))

    # part2 file
    with open("part2.py", "w") as f:
        f.write(template.render(day_number=day_number, part_number="2"))

    # return to the root directory
    os.chdir("..")

    return 0 # No error