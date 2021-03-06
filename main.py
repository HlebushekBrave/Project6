def len_num(n):
    """
    Checks the length of the number
    :param n: number of the card
    """
    i = 0
    while i != 1:
        try:
            n = int(n)
            n = str(n)
            if 13 <= len(n) <= 16:
                i = 1
            else:
                n = input('Введен слишком короткий или слишком длинный номер. Пожалуйста, повторите попытку: ')
                i = 0
        except ValueError:
            n = input('Ошибка при вводе. Пожалуйста, повторите попытку: ')
            i = 0
            continue


def type_of_card(n):
    """
    Checks the type of card
    :param n: number of the card
    """
    if n[0] == '4':
        print('Карта Visa')
    elif n[0] == '5':
        print('Карта MasterCard')
    elif n[0:1] == '37':
        print('Карта American Express')
    elif n[0] == '6':
        print('Карта Discover')
    elif n[0] == '2':
        print('Карта национальной платежной системы "Мир"')
    else:
        print('Карта неизвестного типа')
        exit()


def check(n):
    """
    Сhecks the correctness of the number
    :param n: number of the card
    """
    l = len(n)
    a = list(n[1:l:2])
    r = [int(i) for i in a]
    b = [i*2 for i in r]
    numbers = []
    for elem in b:
        if elem >= 10:
            elem1 = sum(map(int, str(elem)))
            elem1 = int(elem1)
            numbers.append(elem1)
        else:
            numbers.append(elem)
    summ = 0
    for num in numbers:
        summ += num
    if summ % 10 == 0:
        print('Номер карты введен правильно')
    else:
        print('Номер карты введен неверно')


n = str(input('Введите номер карты без пробелов: '))
len_num(n)
type_of_card(n)
check(n)
