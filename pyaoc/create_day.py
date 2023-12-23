import os

def create_day(day_number: int = 1) -> int:
    """Create a new directory for a new day

    Args:
        day_number (int, optional): Day number. Defaults to 1.
    
    Returns:
        int: Error code
    """
    # Check if the day number is valid
    if day_number < 1 or day_number > 25:
        return 1 # Error code 1
    
    # Create the directory
    dir_name = f"day{day_number:02d}"

    # Check if the directory already exists
    if os.path.exists(dir_name):
        return 2 # Error code 2
    
    # Create folders

    os.mkdir(dir_name)
    os.chdir(dir_name)

    # Part1 folder
    if os.path.exists("part1"):
        return 3
    os.mkdir("part1")

    # Part2 folder
    if os.path.exists("part2"):
        return 4
    os.mkdir("part2")

    # Input folder
    if os.path.exists("inputs"):
        return 5
    os.mkdir("inputs")

    # Benchmark folder
    if os.path.exists("benchmark"):
        return 6
    os.mkdir("benchmark")


    # Create files

    # input and sample files
    os.chdir("inputs")
    with open("input.txt", "w") as f:
        pass
    with open("sample.txt", "w") as f:
        pass
    os.chdir("..")

    # part1 file
    os.chdir("part1")
    with open("part1.py", "w") as f:
        pass
    os.chdir("..")

    # part2 file
    os.chdir("part2")
    with open("part2.py", "w") as f:
        pass
    os.chdir("..")

    # return to the root directory
    os.chdir("..")

    return 0 # No error