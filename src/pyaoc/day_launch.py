# This file contains functions to run a day of Advent of Code
import logging
import os
import time
from pyaoc.check_day import check_day_structure, check_name_folder
from importlib.util import spec_from_file_location, module_from_spec

# Logger
logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')


def run_specific_day(day_number: int = 1, timed: bool = False) -> int:
    """Run a specific day of Advent of Code.

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param int day_number: Number of the day. Corresponding directory must exist.
    :param bool timed: The run is timed.
    
    :return: error
    :rtype: int
    """
    if type(day_number) != int:
        logging.error("Invalid day number : day_number must be an int")
        return 1
    
    if type(timed) != bool:
        logging.error("Invalid timed : timed must be an bool")
        return 1

    if day_number < 1 or day_number > 25:
        logging.error("Invalid day number : day_number must be between 1 and 25")
        return 1
    
    if not check_day_structure(day_number):
        return 1
    
    dir_name = f"day{day_number:02d}"

    os.chdir(dir_name)

    text_input = open(os.path.join("inputs", "input.txt"), "r").read()

    # Part 1
    spec = spec_from_file_location("part1", "part1.py")
    part1 = module_from_spec(spec)
    spec.loader.exec_module(part1)

    if timed:
        start_p1 = time.time()
    res_p1 = part1.solution(text_input)
    if timed:
        end_p1 = time.time()
    print(f"Part 1: {res_p1}")
    if timed:
        print(f"Part 1 execution time: {end_p1 - start_p1:.5f}s")

    # Part 2
    spec = spec_from_file_location("part2", "part2.py")
    part2 = module_from_spec(spec)
    spec.loader.exec_module(part2)

    if timed:
        start_p2 = time.time()
    res_p2 = part2.solution(text_input)
    if timed:
        end_p2 = time.time()
    print(f"Part 2: {res_p2}")
    if timed:
        print(f"Part 2 execution time: {end_p2 - start_p2:.5f}s")

    os.chdir("..")
    
    return 0

def run_specific_part_specific_day(part_number: int = 1, day_number: int = 1, timed: bool = False) -> int:
    """Run a specific part of a specific day of Advent of Code.

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param int part_number: Number of the part. Corresponding file must exist.
    :param int day_number: Number of the day. Corresponding directory must exist.

    :return: error
    :rtype: int
    """
    if type(day_number) != int:
        logging.error("Invalid day number : day_number must be an int")
        return 1
    
    if type(part_number) != int:
        logging.error("Invalid part number : part_number must be an int")
        return 1
    
    if type(timed) != bool:
        logging.error("Invalid timed : timed must be an bool")
        return 1

    if day_number < 1 or day_number > 25:
        logging.error("Invalid day number : day_number must be between 1 and 25")
        return 1

    if part_number < 1 or part_number > 2:
        logging.error("Invalid part number : part_number must be between 1 and 2")
        return 1
    
    if not check_day_structure(day_number):
        return 1
    
    dir_name = f"day{day_number:02d}"

    os.chdir(dir_name)

    text_input = open(os.path.join("inputs", "input.txt"), "r").read()

    spec = spec_from_file_location(f"part{part_number}", f"part{part_number}.py")
    part = module_from_spec(spec)
    spec.loader.exec_module(part)

    if timed:
        start = time.time()
    res = part.solution(text_input)
    if timed:
        end = time.time()
    print(f"Part {part_number}: {res}")
    if timed:
        print(f"Part {part_number} execution time: {end - start:.5f}s")
    
    os.chdir("..")

    return 0


def run_current(timed: bool = False) -> int:
    """Run the current day of Advent of Code.

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param bool timed: The run is timed.
        
    :return: error
    :rtype: int
    """
    if type(timed) != bool:
        logging.error("Invalid timed : timed must be an bool")
        return 1

    # Get the current day
    current_path = os.getcwd()
    current_day = os.path.basename(current_path)
    
    if not check_name_folder(current_day):
        return 1
    
    day_number = current_day[3:]
    day_number = int(day_number)


    os.chdir("..")
    err = run_specific_day(day_number, timed)
    os.chdir(current_path)
    return err

def run_current_specific_part(part_number: int = 1, timed: bool = False) -> int:
    """Run a specific part of the current day of Advent of Code.

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param int part_number: Number of the part. Corresponding file must exist.
    :param bool timed: The run is timed.

    :return: error
    :rtype: int
    """
    if type(part_number) != int:
        logging.error("Invalid part number : part_number must be an int")
        return 1
    
    if type(timed) != bool:
        logging.error("Invalid timed : timed must be an bool")
        return 1
    
    if part_number < 1 or part_number > 2:
        logging.error("Invalid part number : part_number must be between 1 and 2")
        return 1
    
    # Get the current day
    current_path = os.getcwd()
    current_day = os.path.basename(current_path)
    
    if not check_name_folder(current_day):
        return 1
    
    day_number = current_day[3:]
    day_number = int(day_number)

    os.chdir("..")
    err = run_specific_part_specific_day(part_number, day_number, timed)
    os.chdir(current_path)
    return err