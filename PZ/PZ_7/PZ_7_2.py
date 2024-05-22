'''Дана строка-предложение на русском языке. Вывести самое короткое слово в
предложении. Если таких слов несколько, то вывести последнее из них. Словом
считать набор символов, не содержащий пробелов, знаков препинания и
ограниченный пробелами, знаками препинания или началом/концом строки.'''
def shortest_word(sentence):
    sentence = ''.join(word for word in sentence if word.isalnum() or word.isspace())
    words = sentence.split()
    shortest = min(words, key=len)
    shortest_words = [word for word in words if len(word) == len(shortest)]
    return shortest_words[-1]

sentence = input("Введите предложение: ")
print(shortest_word(sentence))