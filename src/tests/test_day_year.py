from pyaoc.day_year import get_last_aoc_year


def test_get_last_aoc_year():
    # This test must be valid until 1st decembre 2024 (at 0am EST)
    assert get_last_aoc_year() == 2023
    
