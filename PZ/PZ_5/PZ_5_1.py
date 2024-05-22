''' Составить функцию, которая выполнит суммирование числового ряда'''

def ssum(a,s):
    print(f'Сумма ряда: {sum([i * s for i in range(a + 1)]):.3f}')

try:
    amo = int(input('Введите количество шагов: '))
    step = float(input('Введите шаг: '))
    ssum(amo, step)
except:
    print('Неверное число')