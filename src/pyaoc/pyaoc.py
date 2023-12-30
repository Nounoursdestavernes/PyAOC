import argparse
import logging
import sys
from pyaoc.day_benchmark import benchmark_specific_day
from pyaoc.day_creation import create_day, create_day_force
from pyaoc.day_launch import run_specific_day, run_specific_part_specific_day, run_current, run_current_specific_part
from pyaoc.day_year import get_last_aoc_year
from pyaoc.readme_generation import generate_readme

VERSION = "0.0.1"

logger = logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Add the arguments
    parser.add_argument('--create-day', '-d', type=int, metavar="DAY", help = 'Create a new day')
    parser.add_argument('--force', '-f', action='store_true', help = 'Force the creation of a new day')
    parser.add_argument('--run', '-r', type=int, metavar="DAY", help='Run a specific day')
    parser.add_argument('--run-current', '-rc', action='store_true', help='Run the current day folder')
    parser.add_argument('--part', '-p', type=int, metavar="PART", help='Run a specific part of a specific day')
    parser.add_argument('--time', '-t', action='store_true', help='Print the execution time of each part')
    parser.add_argument('--benchmark', '-b', type=int, nargs=2, metavar=("DAY", "ITERATIONS"), help='Run a specific day with a specific number of iterations')
    parser.add_argument('--year', '-y', type=int, metavar="YEAR", help="Override the current year for the command")
    parser.add_argument('--readme', action="store_true", help="Generate the README file")
    parser.add_argument('--version', action='version', version=f'pyaoc {VERSION}')
    
    # Parse the arguments
    args = parser.parse_args()

    if len(sys.argv) == 1: # No arguments
        parser.print_help()
        return 0
    

    if args.force and not args.create_day:
        logging.error("Force option can only be used with create-day option")
        return 1
    
    if args.part and not (args.run or args.run_current):
        logging.error("Part option can only be used with run option")
        return 1
    
    if args.time and not (args.run or args.run_current):
        logging.error("Time option can only be used with run option or run-current option")
        return 1
    
    if args.run and args.run_current:
        logging.error("Run option and run-current option are mutually exclusive")
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
        
    if args.run_current:
        if args.part:
            err = run_current_specific_part(args.part, args.time)
        else:
            err = run_current(args.time)
            
        if err:
            return 1 

    if args.benchmark:
        err = benchmark_specific_day(args.benchmark[0], args.benchmark[1])
        if err:
            return 1
        
    year = get_last_aoc_year()
    if args.year:
        year = args.year

    if args.readme:
        err = generate_readme()
        if err:
            return 1
        else:
            print("README generated")
    return 0
