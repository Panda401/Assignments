from functions import func11


def main():
    print('-------------------------------')
    print('|      Year    | Revenue/Loss |')
    print('-------------------------------')
    y = []
    # loop executes from k == 0 inclusive to 11 exclusive with the step of 1
    for k in range(0, 11, 1):
        y.append(func11(1991 + k))
        # array index starts with 0
        print('|{:14.0f}|{:14.5f}|'.format(1991 + k, y[k]))
    print('-------------------------------')

    total_losses = 0
    max_loss = 0
    max_loss_year_index = -1
    for idx, x in enumerate(y):
        if x < 0:
            total_losses += x
            # maximum loss is the smallest negative value
            if max_loss > x:
                max_loss = x
                max_loss_year_index = idx

    if max_loss_year_index >= 0:
        print('Total amount of losses for 10 years is: {:.5}'.format(total_losses))
        print('Maximum loss of: {:.5} was in the year: {}'.format(max_loss, 1991 + max_loss_year_index))
    else:
        print('No years with losses found')


if __name__ == '__main__':
    main()
