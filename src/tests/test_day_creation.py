import pytest
import shutil
from pyaoc.day_creation import create_day, create_day_force

# We assume that no day folder exists (clean environment)

# Tests for create_day
def test_create_day():
    assert create_day(1) == None
    shutil.rmtree("day01")

def test_create_day_already_exists():
    assert create_day(1) == None
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        create_day(1)
    assert pytest_wrapped_e.type == SystemExit
    shutil.rmtree("day01")

def test_create_day_out_of_range():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        create_day(0)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        create_day(26)
    assert pytest_wrapped_e.type == SystemExit

def test_create_day_negative():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        create_day(-1)
    assert pytest_wrapped_e.type == SystemExit

def test_create_day_no_args():
    assert create_day() == None
    shutil.rmtree("day01")

def test_create_day_not_int():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        create_day("a")
    assert pytest_wrapped_e.type == SystemExit


# Tests for create_day_force
def test_create_day_force():
    assert create_day_force(1) == None
    assert create_day_force(1) == None
    shutil.rmtree("day01")

def test_create_day_force_out_of_range():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        create_day_force(0)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        create_day_force(26)
    assert pytest_wrapped_e.type == SystemExit

def test_create_day_force_negative():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        create_day_force(-1)
    assert pytest_wrapped_e.type == SystemExit

def test_create_day_force_no_args():
    assert create_day_force() == None
    shutil.rmtree("day01")

def test_create_day_force_not_int():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        create_day_force("a")
    assert pytest_wrapped_e.type == SystemExit