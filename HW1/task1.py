if __name__ == '__main__':
    x = int(input('Введите x: '))
    y = int(input('Введите y: '))

    print(f'Сумма: {x + y}')
    print(f'Разность: {x - y}')
    print(f'Произведение: {x * y}')
    if y == 0:
        print(f'Деление: делить на 0 нельзя')
        print(f'Остаток от деления: делить на 0 нельзя')
    else:
        print(f'Деление: {x / y}')
        print(f'Остаток от деления: {x % y}')
    print(f'x в степени y: {pow(x, y)}')


