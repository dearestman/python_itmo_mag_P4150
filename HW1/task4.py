if __name__ == '__main__':

    oddNumbers = list(range(1, 60, 2))
    print(f'список нечетных значений от 1 до 60: {oddNumbers}')
    divide3or5andNotDivide15 = []

    for num in oddNumbers:
        if ((num % 3 == 0 or num % 5 ==0) and num % 15 != 0):
            divide3or5andNotDivide15.append(num)

    print(f'числа, делящиеся на 3 или на 5 и при этом не делящиеся на 15: {divide3or5andNotDivide15}')
    print(f'последний элемент созданного списка: {divide3or5andNotDivide15[len(divide3or5andNotDivide15)-1]}')
