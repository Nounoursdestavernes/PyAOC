import argparse
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


    if len(sys.argv) == 1: # No arguments
        parser.print_help()
        return 0

    if args.create_day:
        if args.force:
            err = create_day_force(args.create_day)
        else:
            err = create_day(args.create_day)

        if err:
            return 1
        else:
            print(f"Day {args.create_day} created")




    return 0
                


if __name__ == "__main__":
    main()



