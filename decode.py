import cli
def decode(s):
    return ''.join(cli.DICTIONARY_REVERSED.get(i) for i in s.split())