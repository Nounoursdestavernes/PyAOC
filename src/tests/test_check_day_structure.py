import os
import shutil
from pyaoc.check_day_structure import check_day


def test_day_check_day_no_day_folder():
    assert check_day(day_number=1) == 1

def test_day_check_day_no_inputs_folder():
    os.mkdir("day01")
    assert check_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_no_input_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    assert check_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_no_part1_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    assert check_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_no_part2_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")

    assert check_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_no_check_day_folder():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")
    with open(os.path.join("day01", "part2.py"), "w") as f:
        f.write("def solution(text): return 0")
    
    assert check_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_no_check_day_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")
    with open(os.path.join("day01", "part2.py"), "w") as f:
        f.write("def solution(text): return 0")
    os.mkdir(os.path.join("day01", "benchmark"))

    assert check_day(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day():
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
    assert check_day(day_number=1) == 0
    shutil.rmtree("day01")
