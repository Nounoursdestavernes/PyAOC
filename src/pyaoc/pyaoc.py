import argparse
import logging
import sys
from pyaoc.day_creation import create_day, create_day_force
from pyaoc.day_launch import run_specific_day, run_specific_part_specific_day

VERSION = "0.0.1"

logger = logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Add the arguments
    parser.add_argument('--create-day', '-d', type=int, help = 'Create a new day')
    parser.add_argument('--force', '-f', action='store_true', help = 'Force the creation of a new day')
    parser.add_argument('--run', '-r', type=int, help='Run a specific day')
    parser.add_argument('--part', '-p', type=int, help='Run a specific part of a specific day')
    parser.add_argument('--time', '-t', action='store_true', help='Print the execution time of each part')
    parser.add_argument('--version', action='version', version=f'pyaoc {VERSION}')
    
    # Parse the arguments
    args = parser.parse_args()


    if len(sys.argv) == 1: # No arguments
        parser.print_help()
        return 0
    

    if args.force and not args.create_day:
        logging.error("Force option can only be used with create-day option")
        return 1
    
    if args.part and not args.run:
        logging.error("Part option can only be used with run option")
        return 1
    
    if args.time and not args.run:
        logging.error("Time option can only be used with run option")
        return 1

    if args.create_day:
        if args.force:
            err = create_day_force(args.create_day)
        else:
            err = create_day(args.create_day)

        if err:
            return 1
        else:
            print(f"Day {args.create_day} created")
    
    if args.run:
        if args.part:
            err = run_specific_part_specific_day(args.part, args.run, args.time)
        else:
            err = run_specific_day(args.run, args.time)
            
        if err:
            return 1



    return 0
