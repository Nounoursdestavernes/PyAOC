# PyAOC
Python Advent of Code package

## Architecture of a day folder
```text
day{day_number}/
    ├── benchmark/          # Benchmark files for the project
    │   └── benchmark.txt   # Benchmark file for the project   
    ├── inputs/             # Input files for the project
    │   ├── input.txt       # Input file for the project
    │   └── sample.txt      # Sample input file for the project    
    ├── part1/
    │   └── part1.py        # Part 1 of the project
    ├── part2/
    │   └── part2.py        # Part 2 of the project
```
You can create a day folder by running 

```bash
pyaoc {day_number}
```

