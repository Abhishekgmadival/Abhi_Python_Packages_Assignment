# Python Packages – Questions and Answers

## 1. What is a package in Python?
A **package** is a directory that organizes related Python modules. It usually contains an `__init__.py` file
to indicate that the directory should be treated as a package.

## 2. Difference between a module and a package
- **Module**: A single `.py` file (e.g., `math.py`) containing functions, classes, variables.
- **Package**: A directory containing modules and an `__init__.py` file (e.g., `mypkg/`).

## 3. Purpose of `__init__.py`
- Marks the directory as a package.
- Optionally runs initialization code and controls exported names via `__all__`.

## 4. Five built-in Python packages and uses
- `math` — mathematical functions (sqrt, sin, cos, etc.)
- `os` — interacting with the operating system (file paths, directories)
- `sys` — system-specific parameters and command-line arguments
- `random` — random number generation and selection
- `datetime` — dates and times handling

## 5. Difference between:
a) `import math`
   - Imports the whole module. Use `math.sqrt(25)`.
b) `from math import sqrt`
   - Imports only `sqrt`; use directly as `sqrt(25)`.
