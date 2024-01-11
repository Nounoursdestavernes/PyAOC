# This file contains functions to test a day folder structure
import os
import sys
from pyaoc.check_parameters import check_day_number

def check_day_structure(day_number: int = 1) -> None:
    """Check the structure of a day folder

    Return None if the structure is valid, else sys.exit
    
    :param int day_number: Number of the day.

    :return: None
    :rtype: None
    """
    check_day_number(day_number)

    dir_name = f"day{day_number:02d}"

    if not os.path.exists(dir_name):
        sys.exit(f"Directory {dir_name} does not exist")
    
    os.chdir(dir_name)

    if not os.path.exists("inputs"):
        os.chdir("..")
        sys.exit(f"Directory {dir_name}/inputs does not exist")

    os.chdir("inputs")
    if not os.path.exists("input.txt"):
        os.chdir("..") # Go back to day folder
        os.chdir("..") # Go back to src folder
        sys.exit(f"File {dir_name}/inputs/input.txt does not exist")
    
    os.chdir("..")

    if not os.path.exists("part1.py"):
        os.chdir("..")
        sys.exit("File part1.py does not exist")    

    if not os.path.exists("part2.py"):
        os.chdir("..")
        sys.exit("File part2.py does not exist")    

    if not os.path.exists("benchmark"):
        os.chdir("..") # Go back to src folder
        sys.exit(f"Folder {dir_name}/benchmark does not exist")

    if not os.path.exists(os.path.join("benchmark", "benchmark.txt")):
        os.chdir("..") # Go back to src folder
        sys.exit(f"File {dir_name}/benchmark/benchmark.txt does not exist")
    
    os.chdir("..")

    return None

def check_name_folder(name: str) -> None:
    """Check that the folder have a name in following format : day{day_number}

    Where {day_number} is a number between 01 and 25.

    :param int name: Name of the folder.

    :return: None
    :rtype: None
    """
    if len(name) != 5:
        sys.exit("Invalid name : name must be in following format : day{day_number}")
    
    day_number = name[3:]
    if name[:3] != 'day' and not day_number.isdigit():
        sys.exit("Invalid name : name must be in following format : day{day_number}")
    
    day_number = int(day_number)

    if day_number < 1 or day_number > 25:
        sys.exit("Invalid name : day_number must be between 1 and 25")
    
    return None