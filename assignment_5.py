import math


def main():
    drachma = math.fabs(float(input('Enter start drachma value: ')))
    drachma_step = math.fabs(float(input('Enter increment value: ')))
    output_lines = int(math.fabs(int(input('Enter max number of lines in the output (1-15): '))))
    if output_lines > 15:
        print('Invalid number of lines: ' + str(output_lines))
        exit(1)

    print('----------------------------------------------------------')
    print('|     drachma      |       gram       |       ounce      |')
    print('----------------------------------------------------------')
    for n in range(output_lines):
        print('|{:18.5f}|{:18.5f}|{:18.5f}|'.format(drachma, drachma * 1.77185, drachma * 0.06249))
        drachma += drachma_step
    print('----------------------------------------------------------')

if __name__ == '__main__':
    main()
