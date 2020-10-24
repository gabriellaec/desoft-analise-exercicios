def lista_caracteres(string):
    caracteres = []
    i = 0
    while i < len(string):
        caracter = string[i]
        if caracter not in caracteres:
            caracteres.append(caracter)
        i += 1
    return caracteres