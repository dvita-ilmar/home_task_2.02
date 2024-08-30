'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №2.2
Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
'''
# Блок ввода целых чисел
first = int(input('введите первое целое число:'))
second = int(input('введите второе целое число:'))
third = int(input('введите третье целое число:'))

# Блок логики и вывода результатов
if first == second and first == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')
