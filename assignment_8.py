from functions import func10


def main():
    print('-------------------------------')
    print('|      X       |       Y      |')
    print('-------------------------------')
    x = 0.0
    sum = 0.0
    product = 1.0
    while x <= 2:
        y = func10(x)
        if 0 < y < 3.2:
            sum += y
            product *= y

        print('|{:14.5f}|{:14.5f}|'.format(x, y))
        x += 0.2
    print('-------------------------------')

    if sum > 0:
        print('Sum: {} | Product: {}'.format(sum, product))
    else:
        print('No values of Y satisfy condition: 0 < Y < 3.2')


if __name__ == '__main__':
    main()
