'''Дана непустая строка S и целое число N (> 0). Вывести строку, содержащую символы
строки S, между N символами которых вставлена «*» (звездочка).'''

def insert_(s, n):
    return '*'.join([s[i:i+n] for i in range(0, len(s), n)])

while True:
    s = input("Введите строку: ")
    n = input("Введите число: ")
    if n.isdigit():
        n = int(n)
        print(insert_(s, n))
        break
    else:
        print("Пожалуйста, введите действительное число.")
