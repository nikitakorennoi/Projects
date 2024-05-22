'''Дано целое число N (>0). Найти значение выражения 1.1 - 1.2 + 1.3 - ... 
(N слагаемых, знаки чередуются).'''

def calculate_expression(n):
    result = 0
    for i in range(1, n+1):
        result += ((-1)**(i+1)) * (1 + i/10)
    return result

while True:
    try:
        N = abs(int(input("Введите число N: ")))
        result = calculate_expression(N)
        print(f"Значение выражения: {result:.1f}")
        break
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите целое число.")