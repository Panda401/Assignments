import math


def main():
    point_a = (0, 0)
    point_b = (2, 1)
    point_c = (-2, 3)

    length_ab = math.sqrt(math.pow(point_a[0] - point_b[0], 2) + math.pow((point_a[1] - point_b[1]), 2))
    length_bc = math.sqrt(math.pow(point_b[0] - point_c[0], 2) + math.pow((point_b[1] - point_c[1]), 2))
    length_ac = math.sqrt(math.pow(point_a[0] - point_c[0], 2) + math.pow((point_a[1] - point_c[1]), 2))
    half_perimeter = (length_ab + length_bc + length_ac) / 2

    median_a = math.sqrt((2 * length_bc * length_bc + 2 * length_ac * length_ac - length_ab * length_ab) / 4)
    bisector_b = 2 / (length_ab + length_ac) * math.sqrt(
        length_ab * length_ac * half_perimeter * (half_perimeter - length_bc))

    print('Median Ma: ' + str(median_a))
    print('Bisector Wb: ' + str(bisector_b))


if __name__ == '__main__':
    main()
