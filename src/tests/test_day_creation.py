from pyaoc.day_creation import create_day, create_day_force
import shutil

# We assume that no day folder exists (clean environment)

# Tests for create_day
def test_create_day():
    assert create_day(1) == 0
    shutil.rmtree("day01")

def test_create_day_already_exists():
    assert create_day(1) == 0
    assert create_day(1) == 1
    shutil.rmtree("day01")

def test_create_day_out_of_range():
    assert create_day(0) == 1
    assert create_day(26) == 1

def test_create_day_negative():
    assert create_day(-1) == 1

def test_create_day_no_args():
    assert create_day() == 0
    shutil.rmtree("day01")

def test_create_day_not_int():
    assert create_day("a") == 1


# Tests for create_day_force
def test_create_day_force():
    assert create_day_force(1) == 0
    assert create_day_force(1) == 0
    shutil.rmtree("day01")

def test_create_day_force_out_of_range():
    assert create_day_force(0) == 1
    assert create_day_force(26) == 1

def test_create_day_force_negative():
    assert create_day_force(-1) == 1

def test_create_day_force_no_args():
    assert create_day_force() == 0
    shutil.rmtree("day01")

def test_create_day_force_not_int():
    assert create_day_force("a") == 1
