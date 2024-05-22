'''Дано целое число N (> 1).
Вывести наибольшее из целых чисел К,для которых сумма
1 + 2 + ... + К будет меньше или равна N, и саму эту сумму.'''

def find_largest_k(n):
    k = 0
    sum = 0
    while sum <= n:
        k += 1
        sum += k
    return k-1, sum-k

while True:
    try:
        N = int(input("Введите число N: "))
        if N > 1:
            K, sum = find_largest_k(N)
            print("Наибольшее целое число K: ", K)
            print("Сумма чисел от 1 до K: ", sum)
            break
        else:
            print("Пожалуйста, введите целое число больше 1.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите целое число.")