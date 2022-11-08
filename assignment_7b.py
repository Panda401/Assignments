import math
import random

from functions import func9


def main():
    k = 1
    while True:
        a = math.pow(-1, k) * ((func9(k) * math.pow(random.random(), k)) / math.factorial(k))
        k += 1
        if math.fabs(a) <= 0.001:
            break;

    print('Number of steps to achieve 0.001 precision: ' + str(k))


if __name__ == '__main__':
    main()
