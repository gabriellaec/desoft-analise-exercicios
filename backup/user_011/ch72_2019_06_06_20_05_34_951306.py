def lista_caracteres(string):
    caracteres = []
    i = 0
    while i < len(string):
        caracter = string[i].split()
        if caracter not in caracteres:
            caracteres.append(caracter)
    return caracteres