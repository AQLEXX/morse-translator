from cli import DICTIONARY
def to_morse(s):
    return ' '.join(DICTIONARY.get(i.upper()) for i in s)
    print(s)