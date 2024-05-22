'''Дан список размера N. Найти два соседних элемента,
сумма которых максимальна,
и вывести эти элементы в порядке возрастания их индексов.'''
import random

def find_elements(lst):
    if len(lst) < 2:
        return None
    max_sum = lst[0] + lst[1]
    max_index = 0
    for i in range(len(lst)):
        if lst[i-1] + lst[i] > max_sum:
            max_sum = lst[i-1] + lst[i]
            max_index = i - 1
    return lst[max_index], lst[max_index + 1]

try:
    N = int(input("Введите размер списка: "))
    lst = [random.randint(-100, 100) for _ in range(N)]
    print(lst, find_elements(lst))
except:
    print('Введите число!')
    