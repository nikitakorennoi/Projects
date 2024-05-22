'''Дано целое число. 
Вывести его строку-описание вида 
"отрицательное четное число", "нулевое число", "положительное нечетное число" и т.д.'''

def number_description(num):
    if num == 0:
        return "нулевое число"
    elif num > 0:
        if num % 2 == 0:
            return "положительное четное число"
        else:
            return "положительное нечетное число"
    else:
        if num % 2 == 0:
            return "отрицательное четное число"
        else:
            return "отрицательное нечетное число"
try:
    num = int(input("Введите целое число: "))
    description = number_description(num)
    print(description)
except:
    print('Нужно ввести число!')
