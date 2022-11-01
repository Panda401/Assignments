import math

from functions import func6, func5, func4


def main():
    job_type = input('Enter job type (A, B or C): ')
    if job_type not in ('A', 'B', 'C'):
        print("Invalid job type: " + job_type)
        exit(1)

    if job_type == 'A':
        sum_before_tax = 100 * math.fabs(func4(2) + 50)
        tax = sum_before_tax * 0.1
    elif job_type == 'B':
        sum_before_tax = 150 * math.fabs(func5(2) + 100)
        tax = sum_before_tax * 0.15
    else:
        sum_before_tax = 200 * math.fabs(func6(2) + 135)
        tax = sum_before_tax * 0.2

    print('Sum before tax : ' + str(sum_before_tax))
    print('Tax            : ' + str(tax))
    print('Total after tax: ' + str(sum_before_tax - tax))


if __name__ == '__main__':
    main()
