from cli import DICTIONARY
# кодировка в азбуку морзе
def to_morse(s):
    try:
        return ' '.join(DICTIONARY.get(i.upper()) for i in s)
    except (TypeError, ValueError):
        print('Неверное значение, проверьте текстовый файл!')
    