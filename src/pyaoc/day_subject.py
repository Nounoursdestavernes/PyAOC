# This file contains functions to get information about a day of Advent of Code
import requests
import re

def get_day_name(day_number: int = 1, year_number: int = 2023) -> str:
    """Get the name of a specific day of a specific year of the Advent Of Code

    :param int day_number: Number of the day. Must be between 1 and 25
    :param int year_number: Number of the year. Must be between 2015 and current year

    :return: day name
    :rtype: str
    """
    url = f"https://adventofcode.com/{year_number}/day/{day_number}"

    req = requests.get(url)
    full_title = re.findall("<h2>---.*Day \d+:.*---</h2>", req.text)[0] # To get the full day title
    title = re.findall(":\s.*\s", full_title)[0][2:-1]

    return title