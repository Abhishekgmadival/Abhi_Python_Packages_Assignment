# Abhi_Python_Packages_Assignment

This repository contains solutions for the Python Packages & Modules assignment.
It includes three packages and demonstration scripts for each task.

## Structure
```
Abhi_Python_Packages_Assignment/
├── student_tools/
│   ├── __init__.py
│   ├── marks.py
│   ├── grades.py
│   └── details.py
├── sales_tools/
│   ├── __init__.py
│   ├── cleaning.py
│   └── report.py
├── data_summary/
│   ├── __init__.py
│   ├── math_ops.py
│   └── visuals.py
├── mains/
│   ├── main_student.py
│   ├── main_sales.py
│   └── main_summary.py
├── main.py
├── questions.md
├── requirements.txt
└── LICENSE
```

## How to run
1. (Optional) Create a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate    # Windows PowerShell
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run examples:
   ```
   python mains/main_student.py
   python mains/main_sales.py
   python mains/main_summary.py
   ```
4. Or run combined demo:
   ```
   python main.py
   ```

## Notes
- `mains/main_summary.py` will create a plot image (`data_summary/bar_chart.png`) using matplotlib.
- If you push this repo to GitHub, name it `Abhi_Python_Packages_Assignment`.
