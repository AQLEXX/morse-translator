from cli import DICTIONARY_REVERSED
def from_morse(s):
    return ''.join(DICTIONARY_REVERSED.get(i) for i in s.split()).lower()