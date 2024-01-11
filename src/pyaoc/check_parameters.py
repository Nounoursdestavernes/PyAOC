# This file contains functions that check if the parameters are valid.
import sys

def check_day_number(day_number: int = 1) -> None:
    """Checks if the day number is valid. 

    Returns None if the day number is valid, else sys.exit.

    :param int day_number: Number of the day. Must be between 1 and 25.

    :return: None
    :rtype: None
    """
    if type(day_number) != int:
        return sys.exit("Invalid day number : day_number must be an integer")

    if day_number < 1 or day_number > 25:
        return sys.exit("Invalid day number : day_number must be between 1 and 25")
    
    return None

def check_iterations(iterations: int = 1):
    """Checks if the number of iterations is valid. 

    Returns None if the number of iterations is valid, else sys.exit.

    :param int iterations: Number of iterations. Must be an integer.

    :return: None
    :rtype: None
    """
    if type(iterations) != int:
        return sys.exit("Invalid number of iterations : iterations must be an integer")
    
    if iterations < 1:
        return sys.exit("Invalid number of iterations : iterations must be greater than 0")

    return None