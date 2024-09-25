import datetime

if __name__ == '__main__':

    year = 1997
    month = 6
    day = 17

    quarter = 0

    if 1 <= month <= 3:
        quarter = 1
    if 4 <= month <= 6:
        quarter = 2
    if 7 <= month <= 9:
        quarter = 3
    if 10 <= month <= 12:
        quarter = 4

    print(f"квартал года, в котором я родился {quarter}.")

    if 1997 % 4 == 0:
        if 1997 % 100 != 0 or 1997 % 400 == 0:
            print(f'{1997} Год был высокосным')
    else:
        print(f'{1997} Год был не высокосным')

    today = datetime.date.today()
    birthday = datetime.date(year, month, day)
    print(f'Количество дней с даты моего рождения: {(today - birthday).days}')
