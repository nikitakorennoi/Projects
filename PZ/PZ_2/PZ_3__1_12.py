'''Даны три целых числа: A, B, C. Проверить истинность высказывания:
 "Каждое из чисел A, B, C положительное".'''

def number (num1, num2, num3):
    '''Обработчик условия'''
    if num1 > 0 and num2 > 0 and num3 > 0:
        return 'Каждое из чисел положительное'
    elif num1 or num2 or num3 <= 0:
        return 'Одно из чисел не подходит под условие!'

try:
    '''Ошибка при вводе текста'''
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    num3 = int(input('Введите третье число: '))
    descrition = number(num1, num2, num3)
    print(descrition)
except:
    print('Введены неверные данные!')