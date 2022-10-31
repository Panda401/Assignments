import math


def main():
    angle = float(input('Enter angle: '))
    opposite_side = float(input('Enter opposite side length: '))
    adjacent_side = opposite_side / math.tan(math.pi / 180 * angle)

    print('Perimeter: ' + str(((opposite_side + adjacent_side) +
                               math.sqrt(opposite_side * opposite_side + adjacent_side * adjacent_side))))
    print('Ara: ' + str(opposite_side * adjacent_side / 2))


if __name__ == '__main__':
    main()
