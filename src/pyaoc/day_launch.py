import logging
import os
import time
from importlib.util import spec_from_file_location, module_from_spec

# Logger
logger = logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')


def run_specific_day(day_number: int = 1, timed: bool = False) -> int:
    """Run a specific day of Advent of Code.

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param day_number int: Number of the day. Corresponding directory must exist.

    :return: error
    :rtype: int
    """
    if day_number < 1 or day_number > 25:
        logging.error("Invalid day number : RUN_DAY must be between 1 and 25")
        return 1

    dir_name = f"day{day_number:02d}"
    
    if not os.path.exists(dir_name):
        logging.error(f"Directory {dir_name} does not exist")
        return 1
    
    os.chdir(dir_name)

    text_input = open("inputs/input.txt", "r").read()

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
        print(f"Part 1 execution time: {end_p1 - start_p1:.3f}s")

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
        print(f"Part 2 execution time: {end_p2 - start_p2:.3f}s")
    
    return 0

def run_specific_part_specific_day(part_number: int = 1, day_number: int = 1, timed: bool = False) -> int:
    """Run a specific part of a specific day of Advent of Code.

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param part_number int: Number of the part. Corresponding file must exist.
    :param day_number int: Number of the day. Corresponding directory must exist.

    :return: error
    :rtype: int
    """
    if part_number < 1 or part_number > 2:
        logging.error("Invalid part number : PART must be between 1 and 2")
        return 1

    if day_number < 1 or day_number > 25:
        logging.error("Invalid day number : DAY must be between 1 and 25")
        return 1

    dir_name = f"day{day_number:02d}"
    
    if not os.path.exists(dir_name):
        logging.error(f"Directory {dir_name} does not exist")
        return 1
    
    os.chdir(dir_name)

    text_input = open("inputs/input.txt", "r").read()

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
        print(f"Part {part_number} execution time: {end - start:.3f}s")
    
    return 0



