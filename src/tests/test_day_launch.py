import pytest
import os
import shutil
from pyaoc.day_launch import run_specific_day, run_specific_part_specific_day, run_current, run_current_specific_part, run_part

# run_specific_day
def test_run_specific_day_out_of_range():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_specific_day(0)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_specific_day(26)
    assert pytest_wrapped_e.type == SystemExit

def test_run_specific_day_not_int():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_specific_day("a")
    assert pytest_wrapped_e.type == SystemExit

def test_run_specific_day_not_bool():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_specific_day(timed=1)
    assert pytest_wrapped_e.type == SystemExit

def test_run_specific_day_negative_part():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_specific_day(-1)
    assert pytest_wrapped_e.type == SystemExit


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
    assert run_specific_day(1) == None
    shutil.rmtree("day01")

# run_specific_part_specific_day
def test_run_specific_part_specific_day_out_of_range():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_current_specific_part(1, 0)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_current_specific_part(1, 3)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_current_specific_part(0, 1)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_current_specific_part(3, 1)
    assert pytest_wrapped_e.type == SystemExit

def test_run_specific_part_specific_day_not_int():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_specific_part_specific_day("a", 1)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_specific_part_specific_day(1, "a")
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_specific_part_specific_day(1, 1, "a")
    assert pytest_wrapped_e.type == SystemExit

def test_run_specific_part_specific_day_negative_part():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        run_specific_part_specific_day(1, -1)
    assert pytest_wrapped_e.type == SystemExit

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
    assert run_specific_part_specific_day(1, 1) == None
    assert run_specific_part_specific_day(2, 1) == None
    shutil.rmtree("day01")

# run_current
    
def test_run_current_no_day_folder():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_current()
    assert pytest_wrapped_e.type == SystemExit

def test_run_current_wrong_day_folder():
    os.mkdir("day")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_current()
    assert pytest_wrapped_e.type == SystemExit    
    shutil.rmtree("day")
    
def test_run_current_out_of_range_day():
    os.mkdir("day100")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_current()
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("day100")

def test_run_current_wrong_length_day():
    os.mkdir("da")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_current()
    assert pytest_wrapped_e.type == SystemExit
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
    assert run_current() == None
    assert run_current() == None
    os.chdir("..")
    shutil.rmtree("day01")

# run_current_specific_part
    
def test_run_current_specific_part_no_day_folder():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_current_specific_part(1)
    assert pytest_wrapped_e.type == SystemExit

def test_run_current_specific_part_wrong_day_folder():
    os.mkdir("day")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_current_specific_part(1)
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("day")

def test_run_current_specific_part_out_of_range_day():
    os.mkdir("day100")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_current_specific_part(1)
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("day100")

def test_run_current_specific_part_wrong_length_day():
    os.mkdir("da")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_current_specific_part(1)
    assert pytest_wrapped_e.type == SystemExit
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
    assert run_current_specific_part(1) == None
    assert run_current_specific_part(2) == None
    os.chdir("..")
    shutil.rmtree("day01")

# run_part

def test_run_part_no_day_folder():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_part(part_number=1)
    assert pytest_wrapped_e.type == SystemExit

def test_run_part_wrong_day_folder():
    os.mkdir("day")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_part(part_number=1)
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("day")

def test_run_part_out_of_range_day():
    os.mkdir("day100")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_part(part_number=1)
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("day100")

def test_run_part_wrong_length_day():
    os.mkdir("da")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_part(part_number=1)
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("da")

def test_run_part_day():
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
    assert run_part(part_number=1) == (0, -1)
    assert run_part(part_number=2) == (0, -1)
    os.chdir("..")
    shutil.rmtree("day01")

def test_run_part_day_timed():
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
    assert run_part(part_number=1, timed=True)[1] != -1
    os.chdir("..")
    shutil.rmtree("day01")