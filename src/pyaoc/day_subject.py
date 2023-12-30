# This file contains functions to get information about a day of Advent of Code
import requests
import re

def get_day_name(day_number: int = 1, year_number: int = 2023):
    url = f"https://adventofcode.com/{year_number}/day/{day_number}"

    req = requests.get(url)
    full_title = re.findall("<h2>---.*Day \d:.*---</h2>", req.text)[0] # To get the full day title
    title = re.findall(":\s.*\s", full_title)[0][2:-1]

    return title