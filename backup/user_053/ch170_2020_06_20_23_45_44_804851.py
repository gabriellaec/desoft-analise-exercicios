def apaga_repetidos(string):
    caracteres = []
    nova_string = ''
    for letra in string:
        if letra not in caracteres:
            caracteres.append(letra)
            nova_string += letra
        else:
            nova_string += '*'
    return nova_string