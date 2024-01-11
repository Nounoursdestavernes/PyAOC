import os
import pytest
import shutil
from pyaoc.day_benchmark import benchmark_specific_day

def test_day_benchmark_out_of_range():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        benchmark_specific_day(0)
    assert pytest_wrapped_e.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        benchmark_specific_day(26)
    assert pytest_wrapped_e.type == SystemExit

def test_day_benchmark_not_int():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        benchmark_specific_day(day_number="a")
    assert pytest_wrapped_e.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        benchmark_specific_day(day_number=1.5)
    assert pytest_wrapped_e.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        benchmark_specific_day(iterations="a")
    assert pytest_wrapped_e.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        benchmark_specific_day(iterations=1.5)
    assert pytest_wrapped_e.type == SystemExit

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
    assert benchmark_specific_day(day_number=1) == None
    shutil.rmtree("day01")

def test_day_benchmark_negative_iteration():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        benchmark_specific_day(day_number=1, iterations=-1)
    assert pytest_wrapped_e.type == SystemExit