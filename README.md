# PyAOC
Python Advent of Code package

## Author
- Aurélien TRONCY

## Description
PyAOC is a Python package that helps you to optimize your Advent of Code solutions.
It will take care of folder architecture, input files, benchmarking and more.

This repository contains the PyAOC package source code and everything you need to generate the documentation.

## Architecture of the repository

The **source_doc** folder contains the source code for generating the documentation by using sphinx.

The **build_doc** folder contains the generated documentation.

The **src** folder contains the PyAOC package source code.

## For developers
How to work on the PyAOC package.
1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Install the package

### How to clone the repository
```bash
git clone git@github.com:Nounoursdestavernes/PyAOC.git
```

### How to create a virtual environment
```bash
python -m venv venv
```

### How to install dependencies
```bash
pip install -r requirements.txt
```

### How to install the package
Run the following command: (be sure to be in the virtual environment)
```
pip install src/dist/pyaoc-version-py3-none-any.whl
```
Where version is the version of the package you want to install.

### How to generate the documentation
Run the following command: (be sure to be in the virtual environment)
```bash
make html
```
The documentation will be generated in the **build_doc** folder.

If you want to generate the documentation in another format, refer to the sphinx documentation.

