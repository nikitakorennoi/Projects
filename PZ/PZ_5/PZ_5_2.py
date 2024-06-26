'''Описать функцию SortDec3(A, В, С), меняющую содержимое переменных
А, В, С таким образом, чтобы их значения оказались упорядоченными по убыванию
(А, В, С — вещественные параметры, являющиеся одновременно входными и выходными).
С помощью этой функции упорядочить по убыванию два данных набора из трех чисел:
(Al, B1, C1) и (A2, B2, C2).'''

def minis(a, b, c):
    print(f'Упорядоченный по убыванию набор: {sorted([a, b, c])[::-1]}')

try:
    A1, B1, C1 = map(float, input("Введите первый набор: ").split())
    A2, B2, C2 = map(float, input("Введите второй набор: ").split())
    minis(A1, B1, C1)
    minis(A2, B2, C2)
except ValueError:
    print("Неверный ввод")