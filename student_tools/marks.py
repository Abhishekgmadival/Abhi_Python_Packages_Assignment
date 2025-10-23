# marks.py - functions to compute total and average marks

def total_marks(marks_list):
    """Return total of numeric marks in marks_list."""
    if not marks_list:
        return 0
    return sum(marks_list)

def average_marks(marks_list):
    """Return average marks (float). Returns 0 for empty list."""
    if not marks_list:
        return 0.0
    return sum(marks_list) / len(marks_list)
