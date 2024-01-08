import os
import shutil
from pyaoc.day_benchmark import benchmark_specific_day

def test_day_benchmark_out_of_range():
    assert benchmark_specific_day(day_number=0) == 1
    assert benchmark_specific_day(day_number=26) == 1

def test_day_benchmark_not_int():
    assert benchmark_specific_day(day_number="a") == 1
    assert benchmark_specific_day(day_number=1.5) == 1
    assert benchmark_specific_day(iterations='a') == 1
    assert benchmark_specific_day(iterations=1.5) == 1

def test_day_benchmark_no_day_folder():
    assert benchmark_specific_day(day_number=1) == 1

def test_day_benchmark_no_inputs_folder():
    os.mkdir("day01")
    assert benchmark_specific_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_benchmark_no_input_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    assert benchmark_specific_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_benchmark_no_part1_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    assert benchmark_specific_day(day_number=1) == 1
    shutil.rmtree("day01")


def test_day_benchmark_no_part2_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")

    assert benchmark_specific_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_benchmark_no_benchmark_folder():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")
    with open(os.path.join("day01", "part2.py"), "w") as f:
        f.write("def solution(text): return 0")
    
    assert benchmark_specific_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_benchmark_no_benchmark_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")
    with open(os.path.join("day01", "part2.py"), "w") as f:
        f.write("def solution(text): return 0")
    os.mkdir(os.path.join("day01", "benchmark"))

    assert benchmark_specific_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_benchmark():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")
    with open(os.path.join("day01", "part2.py"), "w") as f:
        f.write("def solution(text): return 0")
    os.mkdir(os.path.join("day01", "benchmark"))
    with open(os.path.join("day01", "benchmark", "benchmark.txt"), "w") as f:
        pass
    assert benchmark_specific_day(day_number=1) == 0
    shutil.rmtree("day01")