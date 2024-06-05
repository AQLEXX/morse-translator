import cli
def code(s):
    return ' '.join(cli.DICTIONARY.get(i.upper()) for i in s)