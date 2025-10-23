from student_tools import marks, grades, details

def demo():
    # sample student data
    name = "Abhishek"
    course = "Data Analyst"
    marks_list = [88, 92, 79, 85, 90]  # five subjects

    info = details.student_info(name, course)
    total = marks.total_marks(marks_list)
    avg = marks.average_marks(marks_list)
    grade = grades.assign_grade(avg)

    print(info)
    print(f"Marks: {marks_list}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {avg:.2f}")
    print(f"Grade: {grade}")

if __name__ == '__main__':
    demo()
