def esconde_senha(string):
    for letra in string:
        y = string.replace(letra, '*')
    return y