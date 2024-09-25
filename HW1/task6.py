from math import sqrt

if __name__ == '__main__':

    a = int(input('Введите a: '))
    b = int(input('Введите b: '))
    c = int(input('Введите c: '))

    D = pow(b, 2) - 4 * a * c

    if D < 0 or a == 0:
        print('корней нет')
    elif D == 0:
        x = (-b + sqrt(D)) / (2 * a)
        print(f'корень квадратного уравнения: {x}')
    else:
        sqrtD = sqrt(D)
        x1 = (-b + sqrtD) / (2 * a)
        x2 = (-b - sqrtD) / (2 * a)
        print(f'Корни квадратного уравнения: {x1}, {x2}')