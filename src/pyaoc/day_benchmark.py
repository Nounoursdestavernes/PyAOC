# This file contains functions to benchmark a day of Advent of Code
import logging
import os
import platform
import timeit
from importlib.util import spec_from_file_location, module_from_spec


# Logger
logger = logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')

def benchmark_specific_day(day_number: int = 1, iterations: int = 1000) -> int:
    """Benchmark a specific day of Advent of Code.

    Return an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param int day_number: Number of the day. Corresponding directory must exist.
    :param int iterations: Number of iterations.

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

    spec = spec_from_file_location("part1", "part1.py")
    part1 = module_from_spec(spec)
    spec.loader.exec_module(part1)

    time_p1 = timeit.timeit(lambda: part1.solution(text_input), number=iterations) / iterations
    
    spec = spec_from_file_location("part2", "part2.py")
    part2 = module_from_spec(spec)
    spec.loader.exec_module(part2)

    time_p2 = timeit.timeit(lambda: part2.solution(text_input), number=iterations) / iterations


    with open("benchmark/benchmark.txt", "w") as f:
        f.write(f"System: {platform.system()}\n")
        f.write(f"Processor: {platform.processor()}\n")
        f.write(f"Bit architecture: {platform.architecture()[0]}\n")
        f.write(f"Python version: {platform.python_version()}\n")
        f.write(f"Day: {day_number}\n")
        f.write(f"Part 1: {time_p1:.5f}s mean time for {iterations} iterations\n")
        f.write(f"Part 2: {time_p2:.5f}s mean time for {iterations} iterations\n")

    print(open("benchmark/benchmark.txt", "r").read())

    os.chdir("..")

    return 0