# This file contains functions to run a day of Advent of Code
import os
import time
from pyaoc.check_day import check_day_structure, check_name_folder
from pyaoc.check_parameters import check_day_number, check_timed, check_part_number, check_input_text
from importlib.util import spec_from_file_location, module_from_spec

def run_part(text_input: str = "", part_number: int = 1, timed: bool = False) -> tuple[int, float]:
    """Run a specific part of the current folder.

    Return a tuple composed of the res of the part and the time of the run if the param timed is set to true.

    :param str text_input: Input of the part.
    :param int part_number: Number of the part to run.
    :param bool timed: The run is timed.

    :return: answer and time
    :rtype: tuple[int, float]
    """
    check_input_text(text_input) # Check if text_input is valid
  
    check_part_number(part_number) # Check if part_number is valid

    check_timed(timed) # Check if timed is valid

    current_path = os.getcwd()
    current_day = os.path.basename(current_path)
    check_name_folder(current_day) # Check if the folder have a name in following format : day{day_number}

    spec = spec_from_file_location(f"part{part_number}", f"part{part_number}.py")
    part = module_from_spec(spec)
    spec.loader.exec_module(part)

    if timed:
        start = time.time()
    res = part.solution(text_input)
    if timed:
        end = time.time()
        return (res, end - start)
    
    return (res, -1)


def run_specific_day(day_number: int = 1, timed: bool = False) -> None:
    """Run a specific day of Advent of Code.

    Returns None if the run is successful, else sys.exit.

    :param int day_number: Number of the day. Corresponding directory must exist.
    :param bool timed: The run is timed.
    
    :return: None
    :rtype: None
    """
   
    check_day_number(day_number) # Check if day_number is valid
    
    check_timed(timed) # Check if timed is valid

    check_day_structure(day_number) # Check if the day folder structure is valid
    
    dir_name = f"day{day_number:02d}"

    os.chdir(dir_name)

    text_input = open(os.path.join("inputs", "input.txt"), "r").read()

    # Part 1
    res_p1, time_p1 = run_part(text_input, 1, timed)

    print(f"Part 1: {res_p1}")
    if timed:
        print(f"Part 1 execution time: {time_p1:.5f}s")

    # Part 2
    res_p2, time_p2 = run_part(text_input, 1, timed)
    print(f"Part 2: {res_p2}")
    if timed:
        print(f"Part 2 execution time: {time_p2:.5f}s")

    os.chdir("..")
    
    return None

def run_specific_part_specific_day(part_number: int = 1, day_number: int = 1, timed: bool = False) -> None:
    """Run a specific part of a specific day of Advent of Code.

    Returns None if the run is successful, else sys.exit.

    :param int part_number: Number of the part. Corresponding file must exist.
    :param int day_number: Number of the day. Corresponding directory must exist.

    :return: None
    :rtype: None
    """

    check_part_number(part_number) # Check if part_number is valid

    check_day_number(day_number) # Check if day_number is valid

    check_timed(timed) # Check if timed is valid
    
    check_day_structure(day_number) # Check if the day folder structure is valid
    
    dir_name = f"day{day_number:02d}"

    os.chdir(dir_name)

    text_input = open(os.path.join("inputs", "input.txt"), "r").read()

    res, time_p = run_part(text_input, 1, timed)


    print(f"Part {part_number}: {res}")
    if timed:
        print(f"Part {part_number} execution time: {time_p:.5f}s")
    
    os.chdir("..")

    return None

def run_current(timed: bool = False) -> None:
    """Run the current day of Advent of Code.

    Returns None if the run is successful, else sys.exit.

    :param bool timed: The run is timed.
        
    :return: None
    :rtype: None
    """
    
    check_timed(timed) # Check if timed is valid

    # Get the current day
    current_path = os.getcwd()
    current_day = os.path.basename(current_path)
    
    check_name_folder(current_day)

    day_number = current_day[3:]
    day_number = int(day_number)

    os.chdir("..")
    run_specific_day(day_number, timed)
    os.chdir(current_path)
    return None

def run_current_specific_part(part_number: int = 1, timed: bool = False) -> None:
    """Run a specific part of the current day of Advent of Code.

    Returns None if the run is successful, else sys.exit.

    :param int part_number: Number of the part. Corresponding file must exist.
    :param bool timed: The run is timed.

    :return: None
    :rtype: None
    """
    check_part_number(part_number) # Check if part_number is valid

    check_timed(timed) # Check if timed is valid
    
    # Get the current day
    current_path = os.getcwd()
    current_day = os.path.basename(current_path)
    
    check_name_folder(current_day)
    
    day_number = current_day[3:]
    day_number = int(day_number)

    os.chdir("..")
    run_specific_part_specific_day(part_number, day_number, timed)
    os.chdir(current_path)
    return None