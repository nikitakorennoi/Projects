'''В исходном текстовом найти все даты в форматах ДД.ММ.ГГГГ и
ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
текстовый файл все даты Февраля в формате ДД/ММ/ГГГГ.'''

import re


with open("C:\\Users\\tess\\.vscode\\IS-25\\PZ\\PZ_14\\dates.txt", "r") as file:
    date_txt = file.read()

# Поиск всех дат в формате ДД.ММ.ГГГГ
date_ = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", date_txt)

# Поиск всех дат в формате ДД/ММ/ГГГГ
date_1 = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", date_txt)

count_date_ = len(date_)
count_date_1 = len(date_1)

february_dates = [date for date in date_1 if date[3:5] == "02"]

with open("february_dates.txt", "w") as file:
    for date in february_dates:
        file.write(date + "\n")

print(f"Количество дат в формате ДД.ММ.ГГГГ: {count_date_}")
print(f"Количество дат в формате ДД/ММ/ГГГГ: {count_date_1}")