# This file contains functions to test a day folder structure
import logging
import os

# Logger
logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')


def check_day(day_number: int = 1) -> bool:
    """Check the structure of a day folder

    Return a bool that represents if the structure is correct

    
    :param int day_number: Number of the day.

    :return: validity
    :rtype: bool
    """

    if type(day_number) != int:
        logging.error("Invalid day number : day_number must be an int")
        return 1
    
    if day_number < 1 or day_number > 25:
        logging.error("Invalid day number : day_number must be between 1 and 25")
        return 1

    dir_name = f"day{day_number:02d}"

    if not os.path.exists(dir_name):
        logging.error(f"Directory {dir_name} does not exist")
        return 1
    
    os.chdir(dir_name)

    if not os.path.exists("inputs"):
        logging.error(f"Directory {dir_name}/inputs does not exist")
        os.chdir("..")
        return 1

    os.chdir("inputs")
    
    if not os.path.exists("input.txt"):
        logging.error(f"File {dir_name}/inputs/input.txt does not exist")
        os.chdir("..") # Go back to day folder
        os.chdir("..") # Go back to src folder
        return 1
    
    os.chdir("..")

    if not os.path.exists("part1.py"):
        logging.error("File part1.py does not exist")
        os.chdir("..")
        return 1
    

    if not os.path.exists("part2.py"):
        logging.error("File part2.py does not exist")
        os.chdir("..")
        return 1
    

    if not os.path.exists("benchmark"):
        logging.error(f"Folder {dir_name}/benchmark does not exist")
        os.chdir("..") # Go back to src folder
        return 1
    

    if not os.path.exists(os.path.join("benchmark", "benchmark.txt")):
        logging.error(f"File {dir_name}/benchmark/benchmark.txt does not exist")
        os.chdir("..") # Go back to src folder
        return 1
    
    os.chdir("..")

    return 0