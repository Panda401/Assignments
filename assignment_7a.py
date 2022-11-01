import math

from functions import func9


def main():
    k = 1
    while True:
        a = func9(k) / k
        k += 1
        if math.fabs(a) <= 0.001:
            break

    print('Number of steps to achieve 0.001 precision: ' + str(k))


if __name__ == '__main__':
    main()
