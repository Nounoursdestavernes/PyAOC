import pytest
import os
import shutil
from pyaoc.day_subject import get_day_name, get_input

# Tests for get_day_name

def test_get_day_name_first_december_2020():
    assert get_day_name(1, 2020) == "Report Repair"

def test_get_dany_name_futur():
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        get_day_name(1, 50000)
    assert pytest_wrapped_e.type == SystemExit

def test_get_day_name_past():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_day_name(1, 2014)
    assert pytest_wrapped_e.type == SystemExit

def test_get_day_name_out_of_range():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_day_name(0, 2020)
    assert pytest_wrapped_e.type == SystemExit

def test_get_day_name_negative():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_day_name(-1, 2020)
    assert pytest_wrapped_e.type == SystemExit

def test_get_day_name_no_args():
    assert get_day_name() == "Trebuchet?!"

def test_get_day_name_not_int():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_day_name("a", 2020)
    assert pytest_wrapped_e.type == SystemExit

def test_get_day_name_not_int2():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_day_name(1, "a")
    assert pytest_wrapped_e.type == SystemExit

def test_get_day_name_not_int3():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_day_name("a", "a")
    assert pytest_wrapped_e.type == SystemExit

def test_get_day_name_not_int4():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_day_name("a")
    assert pytest_wrapped_e.type == SystemExit

def test_get_day_name_not_int5():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_day_name(year_number="a")
    assert pytest_wrapped_e.type == SystemExit

def test_get_day_name_not_int6():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_day_name(day_number="a")
    assert pytest_wrapped_e.type == SystemExit

# Tests for get_input
    
def test_get_input_no_secret():
    os.rename("secret.txt", "secret.txt.pyaoc")
    assert get_input() == 1
    os.rename("secret.txt.pyaoc", "secret.txt")

def test_get_input_no_day_folder():
    assert get_input() == 1

def test_get_input_no_input_folder():
    os.mkdir("day01")
    assert get_input() == 1
    os.rmdir("day01")

def test_get_input_no_input_file():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    assert get_input() == 1
    shutil.rmtree("day01")

def test_get_input():
    os.mkdir("day01")
    os.mkdir(os.path.join("day01", "inputs"))
    with open(os.path.join("day01", "inputs", "input.txt"), "w") as f:
        pass
    assert get_input() == 0
    shutil.rmtree("day01")

def test_get_input_negative_day():
    assert get_input(day_number=-1) == 1

def test_get_input_negative_year():
    assert get_input(year_number=-1) == 1

def test_get_input_out_of_range_day():
    assert get_input(day_number=0) == 1

def test_get_input_out_of_range_year():
    assert get_input(year_number=2014) == 1

def test_get_input_not_int_day():
    assert get_input(day_number="a") == 1

def test_get_input_not_int_year():
    assert get_input(year_number="a") == 1

def test_get_input_not_int_day_and_not_int_year():
    assert get_input(day_number="a", year_number="a") == 1

def test_get_input_not_int_day_and_int_year():
    assert get_input(day_number="a", year_number=2020) == 1

def test_get_input_int_day_and_not_int_year():
    assert get_input(day_number=1, year_number="a") == 1

def test_get_input_past_year():
    assert get_input(year_number=2014) == 1

def test_get_input_future_year():
    assert get_input(year_number=50000) == 1