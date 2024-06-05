from cli import DICTIONARY_REVERSED
# декодировка из азбуки морзе
def from_morse(s):
    try:
        return ''.join(DICTIONARY_REVERSED.get(i) for i in s.split()).lower()
    except (TypeError, ValueError):
        print('Неверное значение, проверьте текстовый файл!')