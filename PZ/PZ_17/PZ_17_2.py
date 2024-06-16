import tkinter as tk
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
    N = (random.randint(0, 15))
    lst = [random.randint(-100, 100) for _ in range(N)]
except:
    print('Введите число!')


def show_result():
    result_list = find_elements (lst)
    result_text.delete("1.0", "end")
    result_text.insert("1.0", ''.join(str(result_list)))
    result_text.insert("1.0", ''.join('Элементы с максимальной суммой: '))
    result_text.insert("1.0", ''.join('\n'))
    result_text.insert("1.0", ''.join(str(lst)))
    result_text.insert("1.0", ''.join('Изначальный список: '))
    
root = tk.Tk()
root.title("список нечетных чисел")

personal_frame = tk.LabelFrame(root, text="Найти два соседних эллемента, сумма которых максимальна и вывести эти элементы в порядке возрастания их индексов.")
personal_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

result_text = tk.Text(personal_frame, height=30, width=85)
result_text.grid(row=0, column=0)

button = tk.Button(root, text="Сгенерировать список", command=show_result)
button.grid(row=1, column=0)

root.mainloop()