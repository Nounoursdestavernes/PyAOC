# This file contains functions to get information about a day of Advent of Code
import logging
import os
import requests
import re
import sys


logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')


def get_day_name(day_number: int = 1, year_number: int = 2023) -> str:
    """Get the name of a specific day of a specific year of the Advent Of Code

    :param int day_number: Number of the day. Must be between 1 and 25
    :param int year_number: Number of the year. Must be between 2015 and current year

    :return: day name
    :rtype: str
    """
    url = f"https://adventofcode.com/{year_number}/day/{day_number}"

    req = requests.get(url)

    if req.status_code != 200:
        logging.error(f"Error {req.status_code} while getting day name")
        sys.exit(1)

    full_title = re.findall("<h2>---.*Day \d+:.*---</h2>", req.text)[0] # To get the full day title
    title = re.findall(":\s.*\s", full_title)[0][2:-1]

    return title

def get_input(day_number: int = 1, year_number: int = 2023) -> int:
    """Get the input of a specific day of a specific year of the Advent Of Code
    
    Returns an int that represents if an error occured:
        * 0: No error
        * 1: Error

    :param int day_number: Number of the day. Must be between 1 and 25
    :param int year_number: Number of the year. Must be between 2015 and current year

    :return: error
    :rtype: int
    """

    cookie = open("secret.txt", 'r').read().strip()
    url = f"https://adventofcode.com/{year_number}/day/{day_number}/input"

    req = requests.get(url, cookies={"session": cookie})

    if req.status_code != 200:
        logging.error(f"Error {req.status_code} while getting input")
        return 1
    
    folder_name = f"day{day_number:02d}"
    if not os.path.exists(folder_name):
        logging.error(f"Directory {folder_name} does not exist")
        return 1
    
    os.chdir(folder_name)

    if not os.path.exists("inputs"):
        logging.error(f"Directory {folder_name}/inputs does not exist")
        return 1
    
    if not os.path.exists("inputs/input.txt"):
        logging.error(f"File {folder_name}/inputs/input.txt does not exist")
        return 1
    

    with open("inputs/input.txt", "w") as f:
        f.write(req.text)

    os.chdir("..")
    
    return 0

