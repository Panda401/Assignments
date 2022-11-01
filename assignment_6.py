from functions import func7, func8


def main():
    # from 1 to 7 including 7
    x = 0
    y = 1
    for k in range(1, 8):
        x += func7(k)
        y *= func8(k)

    print('Results: x = {} | y = {} | z = {}'.format(x, y, x * y))


if __name__ == '__main__':
    main()
