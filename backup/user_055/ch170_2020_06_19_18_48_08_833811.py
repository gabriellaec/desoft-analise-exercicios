apaga_repetidos(palavra):
    string = ''
    for c in palavra:
        if c in string:
            string += '*'
        else:
            string += c
    return string