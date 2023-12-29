import logging
import os
from importlib.util import spec_from_file_location, module_from_spec

# Logger
logger = logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')


def run_specific_day(day_number: int = 1) -> int:
    """Run a specific day of Advent of Code.

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param day_number int: Number of the day. Corresponding directory must exist.

    :return: error
    :rtype: int
    """
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
    print(f"Part 1: {part1.solution(text_input)}")

    # Part 2
    spec = spec_from_file_location("part2", "part2.py")
    part2 = module_from_spec(spec)
    spec.loader.exec_module(part2)
    print(f"Part 2: {part2.solution(text_input)}")
    
    return 0

def run_specific_part_specific_day(part_number: int = 1, day_number: int = 1) -> int:
    """Run a specific part of a specific day of Advent of Code.

    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param part_number int: Number of the part. Corresponding file must exist.
    :param day_number int: Number of the day. Corresponding directory must exist.

    :return: error
    :rtype: int
    """
    dir_name = f"day{day_number:02d}"
    
    if not os.path.exists(dir_name):
        logging.error(f"Directory {dir_name} does not exist")
        return 1
    
    os.chdir(dir_name)

    text_input = open("inputs/input.txt", "r").read()

    spec = spec_from_file_location(f"part{part_number}", f"part{part_number}.py")
    part = module_from_spec(spec)
    spec.loader.exec_module(part)
    print(f"Part {part_number}: {part.solution(text_input)}")
    
    return 0



