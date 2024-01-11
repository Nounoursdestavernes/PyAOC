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

def check_iterations(iterations: int = 1) -> None:
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

def check_timed(timed: bool = False) -> None:
    """Checks if the timed parameter is valid. 

    Returns None if the timed parameter is valid, else sys.exit.

    :param bool timed: The run is timed.

    :return: None
    :rtype: None
    """
    if type(timed) != bool:
        return sys.exit("Invalid timed : timed must be an bool")
    
    return None

def check_part_number(part_number: int = 1) -> None:
    """Checks if the part number is valid. 

    Returns None if the part number is valid, else sys.exit.

    :param int part_number: Number of the part. Must be 1 or 2.

    :return: None
    :rtype: None
    """
    if type(part_number) != int:
        return sys.exit("Invalid part number : part_number must be an integer")
    
    if part_number < 1 or part_number > 2:
        return sys.exit("Invalid part number : part_number must be 1 or 2")

    return None

def check_input_text(input_text: str) -> None:
    """Checks if the input text is valid. 

    Returns None if the input text is valid, else sys.exit.

    :param str input_text: Input text.

    :return: None
    :rtype: None
    """
    if type(input_text) != str:
        return sys.exit("Invalid input text : input_text must be a string")
    
    return None