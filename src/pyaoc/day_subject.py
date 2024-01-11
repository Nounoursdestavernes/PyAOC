# This file contains functions to get information about a day of Advent of Code
import logging
import os
import requests
import re
import sys
from pyaoc.check_parameters import check_day_number, check_year_number, check_part_number


logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')


def get_day_name(day_number: int = 1, year_number: int = 2023) -> str:
    """Get the name of a specific day of a specific year of the Advent Of Code

    :param int day_number: Number of the day. Must be between 1 and 25
    :param int year_number: Number of the year. Must be between 2015 and current year

    :return: day_name
    :rtype: str
    """

    check_day_number(day_number)
    
    check_year_number(year_number)

    url = f"https://adventofcode.com/{year_number}/day/{day_number}"

    req = requests.get(url)

    if req.status_code != 200:
        sys.exit(f"Error {req.status_code} while getting day name")

    h2_title = re.findall("<h2>---.*Day [0-9]+:.*---</h2>", req.text)[0] # To get the full day title
    day_name = re.findall(":[ \t\n\r\f\v].*[ \t\n\r\f\v]", h2_title)[0][2:-1]

    return day_name

def get_input(day_number: int = 1, year_number: int = 2023) -> None:
    """Get the input of a specific day of a specific year of the Advent Of Code
    
    Returns None if the input is successfully downloaded, else sys.exit

    :param int day_number: Number of the day. Must be between 1 and 25
    :param int year_number: Number of the year. Must be between 2015 and current year

    :return: error
    :rtype: int
    """

    check_day_number(day_number)

    check_year_number(year_number)

    if not os.path.exists("secret.txt"):
        sys.exit("secret.txt does not exist")
    
    cookie = open("secret.txt", 'r').read().strip()

    dir_name = f"day{day_number:02d}"
    if not os.path.exists(dir_name):
        sys.exit(f"Directory {dir_name} does not exist")
    
    os.chdir(dir_name)

    if not os.path.exists("inputs"):
        os.chdir("..")
        sys.exit(f"Directory {dir_name}/inputs does not exist")
    
    os.chdir("inputs")
    
    if not os.path.exists("input.txt"):
        os.chdir("..") # Go back to day folder
        os.chdir("..") # Go back to src folder
        sys.exit(f"File {dir_name}/inputs/input.txt does not exist")

    url = f"https://adventofcode.com/{year_number}/day/{day_number}/input"
    req = requests.get(url, cookies={"session": cookie})

    if req.status_code != 200:
        sys.exit(f"Error {req.status_code} while getting input")
    
    with open("input.txt", "w") as f:
        f.write(req.text)

    os.chdir("..") # Go back to day folder
    os.chdir("..") # Go back to src folder
    
    return None

def submit(part_number: int = 1, day_number: int = 1, year_number: int = 2023, res: int = 0) -> None:
    """Submit the result of a specific part of a specific day of a specific year of the Advent Of Code

    Returns None if the submission is successful, else sys.exit

    :param int part_number: Number of the part. Must be between 1 and 2
    :param int day_number: Number of the day. Must be between 1 and 25
    :param int year_number: Number of the year. Must be between 2015 and current year
    :param int res: Result to submit

    :return: error
    :rtype: int
    """

    check_day_number(day_number)

    check_part_number(part_number)

    check_year_number(year_number)

    if type(res) != int:
        sys.exit("Invalid result : res must be an int")

    if not os.path.exists("secret.txt"):
        sys.exit("secret.txt does not exist")

    cookie = open("secret.txt", 'r').read().strip()
    
    url = f"https://adventofcode.com/{year_number}/day/{day_number}/answer"
    req = requests.post(url, cookies={"session": cookie}, data={"answer": res, 'level': part_number})

    if req.status_code != 200:
        sys.exit(f"Error {req.status_code} while submitting answer")
    
    if "That's the right answer" in req.text:
        print("Correct answer !")
    elif "That's not the right answer" in req.text:
        print("Wrong answer !")
    elif "You gave an answer too recently" in req.text:
        print("You gave an answer too recently !")
        time = re.findall("You have .* left to wait", req.text)[0]
        print(time)
    elif "You don't seem to be solving the right level" in req.text:
        print("You already solved this level !")
    else:
        print("Unknown error !")

    return None
