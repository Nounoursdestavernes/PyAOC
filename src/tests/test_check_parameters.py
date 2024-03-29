import pytest
from pyaoc.check_parameters import check_day_number, check_iterations, check_timed, check_part_number

# check_day_number
def test_check_day_number_type():
    assert check_day_number(1) == None
    assert check_day_number(25) == None

    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_number("a")
    assert pytest_wrapped_e.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_number(1.5)
    assert pytest_wrapped_e.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_number(True)
    assert pytest_wrapped_e.type == SystemExit

def test_check_day_number_range():
    assert check_day_number(1) == None
    assert check_day_number(25) == None

    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_number(0)
    assert pytest_wrapped_e.type == SystemExit

    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_day_number(26)
    assert pytest_wrapped_e.type == SystemExit

def test_check_day_number_no_args():
    assert check_day_number() == None

def test_check_day_number_negative():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_day_number(-1)
    assert pytest_wrapped_e.type == SystemExit

# check_iterations
    
def test_check_iterations_type():
    assert check_iterations(1) == None
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_iterations("a")
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_iterations(1.5)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_iterations(True)
    assert pytest_wrapped_e.type == SystemExit

def test_check_iterations_range():
    assert check_iterations(1) == None
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_iterations(0)
    assert pytest_wrapped_e.type == SystemExit

def test_check_iterations_no_args():
    assert check_iterations() == None

def test_check_iterations_negative():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_iterations(-1)
    assert pytest_wrapped_e.type == SystemExit

# check_timed

def test_check_timed_type():
    assert check_timed(True) == None
    assert check_timed(False) == None
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_timed("a")
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_timed(1)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_timed(1.5)
    assert pytest_wrapped_e.type == SystemExit

def test_check_timed_no_args():
    assert check_timed() == None

# check_part_number

def test_check_part_number_type():
    assert check_part_number(1) == None
    assert check_part_number(2) == None
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_part_number("a")
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_part_number(1.5)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_part_number(True)
    assert pytest_wrapped_e.type == SystemExit

def test_check_part_number_range():
    assert check_part_number(1) == None
    assert check_part_number(2) == None
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_part_number(0)
    assert pytest_wrapped_e.type == SystemExit
    with pytest.raises(SystemExit) as pytest_wrapped_e: # We expect a SystemExit
        check_part_number(3)
    assert pytest_wrapped_e.type == SystemExit

def test_check_part_number_no_args():
    assert check_part_number() == None

def test_check_part_number_negative():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_part_number(-1)
    assert pytest_wrapped_e.type == SystemExit

