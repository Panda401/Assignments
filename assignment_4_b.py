def main():
    car_model = int(input('Enter model type (1, 2, 3 or 4): '))
    if car_model not in (1, 2, 3, 4):
        print("Invalid car model: " + str(car_model))
        exit(1)

    if car_model == 1:
        print('Car info, year: 1971, price: 500')
    elif car_model == 2:
        print('Car info, year: 1972, price: 700')
    elif car_model == 3:
        print('Car info, year: 2003, price: 5000')
    else:
        print('Car info, year: 2023, price: 85000')


if __name__ == '__main__':
    main()
