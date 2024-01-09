import os
import shutil
from pyaoc.check_day import check_day_structure, check_name_folder

# check_day_structure
def test_day_check_day_no_day_folder():
    assert check_day_structure(day_number=1) == 1

def test_day_check_day_structure_no_inputs_folder():
    os.mkdir("day01")
    assert check_day_structure(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_structure_no_input_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    assert check_day_structure(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_structure_no_part1_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    assert check_day_structure(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_structure_no_part2_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")

    assert check_day_structure(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_structure_no_check_day_structure_folder():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")
    with open(os.path.join("day01", "part2.py"), "w") as f:
        f.write("def solution(text): return 0")
    
    assert check_day_structure(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_structure_no_check_day_structure_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")
    with open(os.path.join("day01", "part2.py"), "w") as f:
        f.write("def solution(text): return 0")
    os.mkdir(os.path.join("day01", "benchmark"))

    assert check_day_structure(day_number=1) == 1
    shutil.rmtree("day01")

def test_day_check_day_structure():
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
    assert check_day_structure(day_number=1) == 0
    shutil.rmtree("day01")

# check_name_folder
    
def test_day_check_name_folder_no_day_folder():
    assert check_name_folder(".") == False

def test_day_check_name_folder_no_inputs_folder():
    assert check_name_folder("day") == False

def test_day_check_name_folder_out_of_range():
    assert check_name_folder("day00") == False
    assert check_name_folder("day26") == False

def test_day_check_name_folder():
    assert check_name_folder("day01") == True
