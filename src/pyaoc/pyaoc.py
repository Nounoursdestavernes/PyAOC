import argparse
import logging
import sys
from pyaoc.day_creation import create_day, create_day_force

VERSION = "0.0.1"

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Add the arguments
    parser.add_argument('--create-day', '-d', type=int, help = 'Create a new day')
    parser.add_argument('--force', '-f', action='store_true', help = 'Force the creation of a new day')
    parser.add_argument('--version', action='version', version=f'pyaoc {VERSION}')
    
    # Parse the arguments
    args = parser.parse_args()


    
    logging.basicConfig(filename="pyaoc.log", level=logging.WARNING, format="%(levelname)s: %(message)s")

    if len(sys.argv) == 1: # No arguments
        parser.print_help()
        return 0

    if args.create_day:
        logging.info(f"Creating day {args.create_day}")
        if args.force:
            logging.info("Force flag set")
            err = create_day_force(args.create_day)
        else:
            err = create_day(args.create_day)

        match err:
            case 0:
                print("Day created successfully")
                logging.info("Day created successfully")
            case 1:
                print("Invalid day number : CREATE_DAY must be between 1 and 25")
                logging.error("Invalid day number : CREATE_DAY must be between 1 and 25")
            case 2:
                print("Directory already exists")
                logging.error("Directory already exists")
            case 3:
                print("Error creating part1 folder")
                logging.error("Error creating part1 folder")
            case 4:
                print("Error creating part2 folder")
                logging.error("Error creating part2 folder")
            case 5:
                print("Error creating inputs folder")
                logging.error("Error creating inputs folder")
            case 6:
                print("Error creating benchmark folder")
                logging.error("Error creating benchmark folder")
            case _:
                print("Unknown error")
                print(f"Error code: {err}")
                logging.error(f"Unknown error, err = {err}")
    
    return 0
                


if __name__ == "__main__":
    main()



