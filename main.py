# Combined demo to run all three tasks
from mains import main_student, main_sales, main_summary

if __name__ == '__main__':
    print('--- Student Tools Demo ---')
    main_student.demo()
    print('\n--- Sales Tools Demo ---')
    main_sales.demo()
    print('\n--- Data Summary Demo ---')
    main_summary.demo()
