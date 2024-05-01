import random

birthday = ['Einstein A. 14.03.1879', 'Mozart W.A. 27.01.1756', 'Shakespeare W. 23.04.1564', 'Curie M. 07.11.1867',
            'Gandhi M. 02.11.1869', 'Napaleon B. 15.08.1769', 'Newton I. 04.01.1643', 'da Vinci L. 15.04.1452',
            'Pushkin A.S. 26.05,1799', 'Darwin C.R. 12.02.1809']

print(birthday[2])

#numbers = [1, 2, 3, 4, 5]
#result = random.sample(numbers, 2)
#print(result[5, 1])


correct = 0
incorrect = 0

'''bornyear1 = input('Year of birth Einstein A.: ')
if bornyear1 == '14.03.1879':
    correct +=1

else:
    incorrect +=1

bornyear2 = input('Year of birth Mozart W.A.: ')
if bornyear2 == '27.01.1756':
    correct +=1
else:
    incorrect +=1

bornyear3 = input('Year of birth Shakespeare W.: ')
if bornyear3 == '23.04.1564':
    correct +=1
else:
    incorrect +=1

bornyear4 = input('Year of birth Curie M.: ')
if bornyear4 == '07.11.1867':
    correct +=1
else:
    incorrect +=1

bornyear5 = input('Year of birth Gandhi M.: ')
if bornyear5 == '02.11.1869':
     correct +=1
else:
     incorrect +=1

bornyear6 = input('Year of birth Napaleon B.: ')
if bornyear5 == '15.08.1769':
     correct +=1
else:
     incorrect +=1

bornyear7 = input('Year of birth Newton I.: ')
if bornyear5 == '04.01.1643':
     correct +=1
else:
     incorrect +=1

bornyear8 = input('Year of birth da Vinci L.: ')
if bornyear5 == '15.04.1452':
     correct +=1
else:
     incorrect +=1

bornyear9 = input('Year of birth Pushkin A.S.: ')
if bornyear5 == '26.05.1799':
     correct +=1
else:
     incorrect +=1

bornyear10 = input('Year of birth Darwin C.R.: ')
if bornyear5 == '12.02.1809':
     correct +=1
else:
     incorrect +=1

print('правильные ответы: ', correct)
print('неправильные ответы: ', incorrect)

famous = 5

prc_correct = (correct/5)*100
prc_incorrect = (incorrect/5)*100

print('процент правильных ответов: ', prc_correct)
print('процент неправильных ответов: ', prc_incorrect)

months = {
    '01': 'январь',
    '02': 'февраль'
}

days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье'
}

date = '02.01.1989'
day, month, year = date.split('.')

print(days[day], months[month], year, 'года')'''