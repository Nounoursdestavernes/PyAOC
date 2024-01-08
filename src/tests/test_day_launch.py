import os
import shutil
from pyaoc.day_launch import run_specific_day, run_specific_part_specific_day, run_current, run_current_specific_part

# run_specific_day
def test_run_specific_day_out_of_range():
    assert run_specific_day(0) == 1
    assert run_specific_day(26) == 1

def test_run_specific_day_not_int():
    assert run_specific_day("a") == 1
    assert run_specific_day(1, 1) == 1

def test_run_specific_day_negative_part():
    assert run_specific_day(-1) == 1

def test_run_specific_day():
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
    assert run_specific_day(1) == 0
    shutil.rmtree("day01")

# run_specific_part_specific_day
def test_run_specific_part_specific_day_out_of_range():
    assert run_specific_part_specific_day(1, 0) == 1
    assert run_specific_part_specific_day(1, 3) == 1
    assert run_specific_part_specific_day(0, 1) == 1
    assert run_specific_part_specific_day(3, 1) == 1

def test_run_specific_part_specific_day_not_int():
    assert run_specific_part_specific_day("a", 1) == 1
    assert run_specific_part_specific_day(1, "a") == 1
    assert run_specific_part_specific_day(1, 1, "a") == 1

def test_run_specific_part_specific_day_negative_part():
    assert run_specific_part_specific_day(-1, 1) == 1

def test_run_specific_part_specific_day():
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
    assert run_specific_part_specific_day(1, 1) == 0
    assert run_specific_part_specific_day(2, 1) == 0
    shutil.rmtree("day01")

# run_current
    
def test_run_current_no_day_folder():
    assert run_current() == 1

def test_run_current_wrong_day_folder():
    os.mkdir("day")
    assert run_current() == 1
    shutil.rmtree("day")
    
def test_run_current_out_of_range_day():
    os.mkdir("day100")
    assert run_current() == 1
    shutil.rmtree("day100")

def test_run_current_wrong_length_day():
    os.mkdir("da")
    assert run_current() == 1
    shutil.rmtree("da")

def test_run_current_day():
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
    os.chdir("day01")
    assert run_current() == 0
    assert run_current() == 0
    os.chdir("..")
    shutil.rmtree("day01")

# run_current_specific_part
    
def test_run_current_specific_part_no_day_folder():
    assert run_current_specific_part(1) == 1

def test_run_current_specific_part_wrong_day_folder():
    os.mkdir("day")
    assert run_current_specific_part(1) == 1
    shutil.rmtree("day")

def test_run_current_specific_part_out_of_range_day():
    os.mkdir("day100")
    assert run_current_specific_part(1) == 1
    shutil.rmtree("day100")

def test_run_current_specific_part_wrong_length_day():
    os.mkdir("da")
    assert run_current_specific_part(1) == 1
    shutil.rmtree("da")

def test_run_current_specific_part_day():
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
    os.chdir("day01")
    assert run_current_specific_part(1) == 0
    assert run_current_specific_part(2) == 0
    os.chdir("..")
    shutil.rmtree("day01")