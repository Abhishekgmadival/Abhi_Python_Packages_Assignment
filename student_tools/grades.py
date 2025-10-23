# grades.py - function to assign grade based on average marks

def assign_grade(avg):
    """Assign grade:
    A for >=90, B for >=75, C for >=50, else 'Fail'
    """
    try:
        avg = float(avg)
    except Exception:
        return "Invalid"

    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"
