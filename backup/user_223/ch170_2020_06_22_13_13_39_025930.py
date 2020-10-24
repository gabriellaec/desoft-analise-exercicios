def apaga_repetidos(string):
    for c in string:
        if c in string:
            c = '*'
    return c