# This file contains functions to create a new day for Advent of Code
import os
import shutil
import sys
from jinja2 import Environment, PackageLoader
from pyaoc.check_parameters import check_day_number

#Jinja2 environment
env = Environment(
    loader=PackageLoader('pyaoc', '.'),
)

def create_day(day_number: int = 1) -> None:
    """Create a new directory for a new day of Advent of Code.

    Returns None if the creation is successful, else sys.exit.
    
    :param int day_number: Number of the day. Must be between 1 and 25.

    :return: None
    :rtype: None
    """

    # Check if the day number is valid
    check_day_number(day_number)

    # Create the directory
    dir_name = f"day{day_number:02d}"


    # Create folders
    if os.path.exists(dir_name):
        return sys.exit(f"Directory {dir_name} already exists")
    
    os.mkdir(dir_name)
    os.chdir(dir_name)

    # Input folder
    if os.path.exists("inputs"):
        os.chdir("..")
        return sys.exit("inputs folder already exists")
    
    os.mkdir("inputs")

    # Benchmark folder
    if os.path.exists("benchmark"):
        os.chdir("..")
        return sys.exit("benchmark folder already exists")
    
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

    return None # No error



def create_day_force(day_number: int = 1) -> int:
    """Create a new directory for a new day of Advent of Code. If the directory already exists, delete it and create a new one.
    
    Returns None if the creation is successful, else sys.exit.

    :param int day_number: Number of the day. Must be between 1 and 25.

    :return: None
    :rtype: None
    """
   
    # Check if the day number is valid
    check_day_number(day_number)
    
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

    return None # No error