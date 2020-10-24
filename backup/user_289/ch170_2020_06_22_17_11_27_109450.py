def apaga_repetidos(string):
    lista_letras = []
    X = len(string)
    for letra in string:
        LETRA = letra.upper()
        if LETRA not in lista_letras:
            lista_letras.append(LETRA)
        else:
            nova_string = string.replace(letra, '*')
    return nova_string        


    