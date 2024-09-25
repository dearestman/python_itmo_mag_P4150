if __name__ == '__main__':

    list = []

    print('Введите числа:')
    while (True):
        num = int(input())
        if (num == -1):
            break
        list.append(num)

    print(f'Длина списка: {len(list)}')

    sum = 0
    honestList = []

    for num in list:
        if (num % 2 == 0):
            honestList.append(num)
        sum+=num

    print(f'Сумма списка: {sum}')
    print(f'Четные элементы списка: {honestList}')
