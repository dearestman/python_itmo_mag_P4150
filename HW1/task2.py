if __name__ == '__main__':
    str = input('Введите слово: ')
    result = ''
    for i in range(len(str)):
        if (i % 2 == 1):
            continue
        if (result == ''):
            result+=str[i]
        else:
            result+=(', ' + str[i])
    print(result)

    print(str[::-1])
