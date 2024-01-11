import argparse
import logging
import sys
from pyaoc.day_benchmark import benchmark_specific_day
from pyaoc.day_creation import create_day, create_day_force
from pyaoc.day_launch import run_specific_day, run_specific_part_specific_day, run_current, run_current_specific_part
from pyaoc.day_subject import get_input, submit
from pyaoc.day_year import get_last_aoc_year
from pyaoc.readme_generation import generate_readme

VERSION = "0.0.2"

logging.basicConfig(level=logging.WARNING, format='%(levelname)s %(message)s')

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Add the arguments
    parser.add_argument('--create-day', '-cd', type=int, metavar="DAY", help = 'Create a new day')
    parser.add_argument('--force', '-f', action='store_true', help = 'Force the creation of a new day')
    parser.add_argument('--run', '-r', type=int, metavar="DAY", help='Run a specific day')
    parser.add_argument('--run-current', '-rc', action='store_true', help='Run the current day folder')
    parser.add_argument('--part', '-p', type=int, metavar="PART", help='Precise the specific part to run or submit')
    parser.add_argument('--year', '-y', type=int, metavar="YEAR", help="Override the current year for the command")
    parser.add_argument('--time', '-t', action='store_true', help='Print the execution time of each part')
    parser.add_argument('--benchmark', '-b', type=int, nargs=2, metavar=("DAY", "ITERATIONS"), help='Run a specific day with a specific number of iterations')
    parser.add_argument('--readme', action="store_true", help="Generate the README file")
    parser.add_argument('--download-input', '-di', type=int, metavar="DAY", help="Download the input of a specific day")
    parser.add_argument('--submit', '-s', type=int, metavar="DAY", help="[NOT IMPLEMENTED] Submit the solution of a specific day (if no part is specified, submit both parts)")
    parser.add_argument('--version', '-v', action='version', version=f'pyaoc {VERSION}')
    
    # Parse the arguments
    args = parser.parse_args()

    if len(sys.argv) == 1: # No arguments
        parser.print_help()
        sys.exit(0)
    
    if args.force and not args.create_day:
        sys.exit("Force option can only be used with create-day option")
    
    if args.part and not (args.run or args.run_current):
        sys.exit("Part option can only be used with run or submit option")
         
    if args.time and not (args.run or args.run_current):
        sys.exit("Time option can only be used with run option or run-current option")
    
    if args.run and args.run_current:
        sys.exit("Run option and run-current option are mutually exclusive")
    
    year = get_last_aoc_year()
    if args.year: # Override the current year if the option is used
        year = args.year

    if args.create_day: # Create a new day
        if args.force: # Force the creation of a new day
            create_day_force(args.create_day)
        else:
            create_day(args.create_day)
        print(f"Day {args.create_day} created")

    ### TODO: Change with the exit code of the function

    if args.download_input:
        get_input(args.download_input, year)
        print(f"Input of day {args.download_input}/{year} downloaded")
    
    if args.run:
        if args.part:
            run_specific_part_specific_day(args.part, args.run, args.time)
        else:
            run_specific_day(args.run, args.time)
        
    if args.run_current:
        if args.part:
            run_current_specific_part(args.part, args.time)
        else:
            run_current(args.time)

    if args.benchmark:
        benchmark_specific_day(args.benchmark[0], args.benchmark[1])
        
    if args.readme:
        generate_readme(year)
        print("README generated")
    
    sys.exit(0)
