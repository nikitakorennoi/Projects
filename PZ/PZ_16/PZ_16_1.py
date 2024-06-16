'''Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
выводит информацию о животном в формате "Имя: имя, Вид: вид".'''

import pickle

class Животное:
    def __init__(self, имя, вид):
        self.имя = имя
        self.вид = вид

    def info(self):
        return f"Имя: {self.имя}, Вид: {self.вид}"

животное = Животное("Барсик", "Кот")
животное2 = Животное('Бобик', 'Собака')
животное3 = Животное('Гена', 'Крокодил')

def save_def(val, file):
    with open(file, 'wb') as f:
        pickle.dump(val, f)


def load_def(file):
    with open(file, 'rb') as f:
        val = pickle.load(f)
    return val


val_info = [животное, животное2, животное3]

for val in val_info:
    save_def(val, 'values.pkl')
    values = load_def('values.pkl')
    print(values.info())