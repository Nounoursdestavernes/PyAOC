# This file contains functions to benchmark a day of Advent of Code
import os
import platform
import timeit
from pyaoc.check_day import check_day_structure
from pyaoc.check_parameters import check_day_number, check_iterations
from importlib.util import spec_from_file_location, module_from_spec


def benchmark_specific_day(day_number: int = 1, iterations: int = 1000) -> int:
    """Benchmark a specific day of Advent of Code.

    Returns None if the benchmark is successful, else sys.exit.

    :param int day_number: Number of the day. Corresponding directory must exist.
    :param int iterations: Number of iterations.

    :return: None
    :rtype: None    
    """

    check_iterations(iterations) # Check if iterations is valid

    check_day_number(day_number) # Check if day_number is valid

    dir_name = f"day{day_number:02d}"

    check_day_structure(day_number) # Check if the day folder structure is valid
    
    os.chdir(dir_name)

    text_input = open(os.path.join("inputs", "input.txt"), "r").read()

    spec = spec_from_file_location("part1", "part1.py")
    part1 = module_from_spec(spec)
    spec.loader.exec_module(part1)

    time_p1 = timeit.timeit(lambda: part1.solution(text_input), number=iterations) / iterations
    
    spec = spec_from_file_location("part2", "part2.py")
    part2 = module_from_spec(spec)
    spec.loader.exec_module(part2)

    time_p2 = timeit.timeit(lambda: part2.solution(text_input), number=iterations) / iterations


    with open(os.path.join("benchmark","benchmark.txt"), "w") as f:
        f.write(f"System: {platform.system()}\n")
        f.write(f"Processor: {platform.processor()}\n")
        f.write(f"Bit architecture: {platform.architecture()[0]}\n")
        f.write(f"Python version: {platform.python_version()}\n")
        f.write(f"Day: {day_number}\n")
        f.write(f"Part 1: {time_p1:.5f}s mean time for {iterations} iterations\n")
        f.write(f"Part 2: {time_p2:.5f}s mean time for {iterations} iterations\n")

    print(open(os.path.join("benchmark","benchmark.txt"), "r").read())

    os.chdir("..")

    return None