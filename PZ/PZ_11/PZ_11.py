from random import randint


'''
Вариант 12.
1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую

обработку элементов:
Исходные данные:
Количество элементов:
Максимальный элемент:
Среднее арифметическое элементов первой трети:

2. Из предложенного текстового файла (textl 8-12.txt) вывести на экран его содержимое,
количество пробельных символов. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно вставив после каждой строки строку из символов "*" '''

with open('C:\\Users\\tess\\.vscode\\IS-25\\PZ\\PZ_11\\file.txt', 'w+') as file:
    file.write(' '.join(str([randint(-10, 10)for i in range(10)])[1:][:-1].split(', ')))
with open('C:\\Users\\tess\\.vscode\\IS-25\\PZ\\PZ_11\\file.txt', 'r+') as file:
    list_ = list(map(int, file.read().split()))
print(list_)

with open('C:\\Users\\tess\\.vscode\\IS-25\\PZ\\PZ_11\\file2.txt', 'w+', encoding='utf-8') as itog:
    itog.write('Исходные данные: '+ str(list_)[1:][:-1] + '\n')
    itog.write('Количество элементов: '+ str(len(list_)) + '\n')
    itog.write('Максимальный элемент: '+ str(max(list_)) + '\n')
    three = ag = (len(list_)//3)
    a = 0
    while (three) > 0:
        a += list_[three-1]
        three = three - 1
    
    itog.write('Среднее значение: '+ str((a/ag)) + '\n')
    

with open ('text18-12.txt', 'r', encoding='utf-8') as f:
    a = f.read()
    cnt = 0
    for i in a:
        if i == ' ':
            cnt += 1
    print(a, cnt, sep='\n')
    f.seek(0)
    
    with open('newfile.txt', 'w+', encoding='utf-8') as nf:
        b = len(f.readlines())
        f.seek(0)
        nf.write(f.readline())
        for i in range(b-1):
            nf.write('*'*15+'\n')
            nf.write(f.readline())