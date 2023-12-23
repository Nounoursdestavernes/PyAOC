import argparse
from pyaoc.create_day import create_day    

def main():
    """Main function
    """
    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Add the arguments
    parser.add_argument("day_number", type=int, help="Day number")

    # Parse the arguments
    args = parser.parse_args()

    # Create the day
    err = create_day(args.day_number)
    match err:
        case 0:
            print("Day created successfully")
        case 1:
            print("Invalid day number")
            print("Day number must be between 1 and 25")
        case 2:
            print("Directory already exists")
        case 3:
            print("Error creating part1 folder")
        case 4:
            print("Error creating part2 folder")
        case 5:
            print("Error creating inputs folder")
        case 6:
            print("Error creating benchmark folder")
        case _:
            print("Unknown error")
            print(f"Error code: {err}")


if __name__ == "__main__":
    main()



