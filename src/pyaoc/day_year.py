# This file contains functions to get the year of Advent of Code

import time

def get_last_aoc_year() -> int:
    """Compute the last Advent Of Code year.

    Return the last Advent Of Code year. If you are in decembre it return the current year.
    Otherwise, it return the last year.

    :return: year
    :rtype: int
    """
    now = time.time()
    est = time.gmtime(now - 5 * 60 * 60) # EST is equal to UTC-5

    current_year = est.tm_year
    current_month = est.tm_mon

    if current_month == 12:
        return current_year
    else:
        return current_year - 1