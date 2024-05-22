'''Дан список размера N и целое число К (1 < К < N). Осуществить сдвиг элементов
списка вправо на К позиций (при этом А1 перейдет в Ak+1, А2 — в Аk+2, ..AN-k — в
АN, а исходное значение К последних элементов будет потеряно). Первые К
элементов полученного списка положить равными 0.'''
import random

def input_():
    while True:
        try:
            N = int(input("Введите N: "))
            k = int(input("Введите K: "))
            if not (1 < k < N):
                print("Ошибка: К должно быть больше 1 и меньше N")
                continue
            lst = [random.randint(-100, 100) for _ in range(N)]
            new_lst = [0]*k + lst[:-k]
            return lst, new_lst
        except ValueError:
            print("Ошибка: введите число")

print(input_())
