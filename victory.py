import random

while True:

    print('Введите пожалуйста дату рождения (дд.мм.гггг) знаменитых людей! ')

    dates_great_people = {'Einstein A.': '14.03.1879',
             'Mozart W.A.': '27.01.1756',
             'Shakespeare W.': '23.04.1564',
             'Curie M.': '07.11.1867',
             'Gandhi M.': '02.11.1869',
             'Napaleon B.': '15.08.1769',
             'Newton I.': '04.01.1643',
             'da Vinci L.': '15.04.1452',
             'Pushkin A.S.': '26.05,1799',
             'Darwin C.R.': '12.02.1809'}

    great_people = list(dates_great_people.keys())
    result = random.sample(great_people, 5)
    print(result)

    correct = []
    incorrect = []

    for man in result:
        date_birth = (input(f'Введите дату рождения {man}: '))
        value = dates_great_people.get(man)
        if date_birth == value:
            print('верно')
            correct_answers.append(value)
        else:
            def get_date(date):
                day_list = ['первое', 'второе', 'третье', 'четвёртое',
                            'пятое', 'шестое', 'седьмое', 'восьмое',
                            'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                            'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                            'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                            'двадцать первое', 'двадцать второе', 'двадцать третье',
                            'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                            'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                            'тридцатое', 'тридцать первое']
                month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
                date_list = date.split('.')
                return (day_list[int(date_list[0]) - 1] + ' ' +
                        month_list[int(date_list[1]) - 1] + ' ' +
                        date_list[2] + ' года')


            date = value
            print(f'День рождения {man} {get_date(date)}')
            incorrect_answers.append(date)

    print('Правильных ответов:', len(correct_answers))
    print('Неправильных ответов:', len(incorrect_answers))

    qwestion = input("Возможно вы хотите повторить?(да/нет) ")
    if qwestion == 'нет':
        break