import pytest
from pyaoc.check_parameters import check_day_number

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