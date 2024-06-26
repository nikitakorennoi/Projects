from random import randint
'''Организовать и вывести последовательность из N случайных целых чисел. Из
исходной последовательности организовать новую последовательность, содержащую
положительные числа. Найти их количество.'''

N = int(input('Задайте желаемое количество чисел: '))
list_ = [randint(-10, 10) for i in range(N)]
print("Исходная последовательность:", list_)
positive_list = [num for num in list_ if num > 0]
print("Положительные числа из последовательности:", positive_list)
count_positive = len(positive_list)
print("Количество положительных чисел:", count_positive)

'''2. Из списка: ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
получить новый список, в котором длина слов не превышает 5 символов.'''

original_names = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
short_names = [name for name in original_names if len(name) <= 5]
print(f"Исходный список имен: {original_names}")
print(f"Новый список с именами длиной не более 5 символов: {short_names}")
