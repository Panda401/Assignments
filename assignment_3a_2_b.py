import math

from functions import func4, func5


def main():
    # x, а, b,c, d
    x = float(input('Enter X: '))
    a = float(input('Enter A: '))
    b = float(input('Enter B: '))
    c = float(input('Enter C: '))
    d = float(input('Enter D: '))

    if math.fabs(x) < 10:
        theta = math.tan(x + a) - math.log2(math.fabs(b + 7))
        print('Value of F: ' + str(func4(theta)))
    else:
        omega = math.pow(c, 5) * math.sqrt(x * x + d * math.pow(math.e, 1.3))
        print('Value of F: ' + str(func5(omega)))


if __name__ == '__main__':
    main()
