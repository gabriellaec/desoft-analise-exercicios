def apaga_repetidos(string):
    lista_letras = []
    X = len(string)
    i = 0 
    while i < X:
        LETRA = string[i].upper()
        if LETRA not in lista_letras:
            lista_letras.append(LETRA)
            i += 1
        else:
            string.replace(string[i], '*')
            i += 1
    return string        


    