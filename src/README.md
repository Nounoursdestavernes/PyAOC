# PyAOC

Python Advent of Code package

## Author
- Aurélien TRONCY

## Description
PyAOC is a Python package that helps you to optimize your Advent of Code solutions. It will take care of folder architecture, input files, benchmarking and more. 

## List of basic features

### Print Help
To print the help of PyAOC, run the following command:
```bash
pyaoc --help
``` 
It will print all the available commands and options of PyAOC.

### Print Version
To print the version of PyAOC, run the following command:
```bash
pyaoc --version
```


### Create a day folder
PyAOC can create a folder for a specific day. 

To do so, run the following command:
```bash
pyaoc --create-day {day_number}
```
Where {day_number} is the number of the day you want to create.

The architecture of the day folder will be the following:
```text
day{day_number}/
    ├── benchmark/
    │   └── benchmark.txt  
    ├── inputs/
    │   ├── input.txt 
    │   └── sample.txt    
    ├── part1.py
    └── part2.py
```
Benchmark file will be used to store the benchmark results of your code. Inputs folder will contain the input.txt file which is the input file given by Advent of Code. You have to paste the content of the input file yourself if you don't configure PyAOC for the advanced features. The sample.txt file is a sample input file that you can use to test your code. part1.py and part2.py are the files where you will write your code.

For example, a part1 file for day 1 will look like this:
```python
# Description: Day 1 Part 1 of Advent of Code 2023


def solution(textfile: str) -> int:

    return 0
```
textfile arg is the text content of the input file. You have to write your code in the solution function. The solution function must return an integer. You can create as many functions as you want in the file. You can also create as many files as you want in the day folder.

### Force create a day folder

If the folder already exists, PyAOC will ask you to add the --force flag to overwrite the folder. If you add the --force flag, the content of the folder will be deleted and replaced by the default content.

### Run your code
PyAOC can run your code on the input file for a specific day.

To do so, you have to be on the parent folder of the day folder you want to run. Then, run the following command:
```bash
pyaoc --run {day_number}
```
Where {day_number} is the number of the day you want to run.

PyAOC will run the part1.py and part2.py files and print the result of each part.

You can also run only one part of the day by adding the --part flag:
```bash
pyaoc --run {day_number} --part {part_number}
```
Where {part_number} is the number of the part you want to run.

You can also run the current day folder by using the --run-current flag:
```bash
pyaoc --run-current
```

### Time your code
PyAOC can time your code on the input file for a specific day.

To do so, you have to be on the parent folder of the day folder you want to time. Then, run the following command:
```bash
pyaoc --run {day_number} --time
```
Where {day_number} is the number of the day you want to time.

You can combine the --time flag with the --part flag to time only one part of the day:
```bash
pyaoc --run {day_number} --time --part {part_number}
```
Where {part_number} is the number of the part you want to time.

### Benchmark
PyAOC can benchmark your code on the input file for a specific day.

To do so, you have to be on the parent folder of the day folder you want to time. Then, run the following command:
```bash
pyaoc --benchmark {day_number} {iterations}
```
Where {day_number} is the number of the day you want to time and {iterations} the number of iterations you want.

### Override year
By default, the year parameter is set to the current year if you are in december and the last year otherwise. This is to match the last possible Advent Of Code.

If you want to override the default value you have to add the --year option
```bash
pyaoc --year {year}
```
Where {year} is the number of the year you want. 

This is usefull for option like ubmit, download of the input, ...

For the moment you have to use this option in each command.

### Generate README
PyAOC can generate the readme of your project.

To do so, you have to be on the parent folder of all the days folders. Then run the following command:
```bash
pyaoc --readme
```

It will auto-generate the README with benchmarks.


## List of advanced features
To use the advanced features, you have to configure PyAOC. To do so, you have to create a secret.txt file in the root folder of your project. This file must contain the cookie of your session. You can find it in the cookie of your browser when you are logged in Advent of Code.

**IMPORTANT !!! Please do NOT push your secret.txt file on internet !**

### Download input
PyAOC can download the input file for a specific day.
```bash
pyaoc --download-input {day_number}
```
Where {day_number} is the number of the day you want to download input.
