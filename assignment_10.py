from functions import func12


def main():
    print('-----------------------------')
    print('|      K      |     Y(K)    |')
    print('-----------------------------')
    y = []
    # loop executes from k == 1 inclusive to 7 exclusive with the step of 1
    for k in range(0, 7, 1):
        y.append(func12(k+1))
        # array index starts with 0
        print('|{:13.0f}|{:13.5f}|'.format(k+1, y[k]))
    print('-------------------------------')

    if y[2] >= 0 and y[5] >= 0:
        print('The sum of 3rd and 6th positive elements is: {:.5}'.format(y[2] + y[5]))
    else:
        print('Array element 3 or 6 or both are negative')


if __name__ == '__main__':
    main()
