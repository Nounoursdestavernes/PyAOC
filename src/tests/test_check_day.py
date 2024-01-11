import os
import shutil
import pytest
from pyaoc.check_day import check_day_structure, check_name_folder

# check_day_structure
def test_day_check_day_no_day_folder():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_structure()
    assert pytest_wrapped_e.type == SystemExit

def test_day_check_day_structure_no_inputs_folder():
    os.mkdir("day01")
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_structure()
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("day01")

def test_day_check_day_structure_no_input_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_structure()
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("day01")

def test_day_check_day_structure_no_part1_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_structure()
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("day01")

def test_day_check_day_structure_no_part2_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    with open(os.path.join("day01", "part1.py"), "w") as f:
        f.write("def solution(text): return 0")

    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_structure()
    assert pytest_wrapped_e.type == SystemExit
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
    
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_structure()
    assert pytest_wrapped_e.type == SystemExit
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

    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_structure()
    assert pytest_wrapped_e.type == SystemExit
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
    assert check_day_structure() == None
    shutil.rmtree("day01")

# check_name_folder
    
def test_day_check_name_folder_no_day_folder():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_name_folder(".")
    assert pytest_wrapped_e.type == SystemExit

def test_day_check_name_folder_no_inputs_folder():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_name_folder("day")
    assert pytest_wrapped_e.type == SystemExit
def test_day_check_name_folder_out_of_range():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_name_folder("day00")
    assert pytest_wrapped_e.type == SystemExit    
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_name_folder("day26")
    assert pytest_wrapped_e.type == SystemExit
    
def test_day_check_name_folder():
    assert check_name_folder("day01") == None
