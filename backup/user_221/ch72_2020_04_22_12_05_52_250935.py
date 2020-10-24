def lista_caracteres(string):
    caracteres = []
    i = 0
    while i < len(string) - 1:
        if not string[i] in caracteres:
            caracteres.append(string[i])
        i = i + 1
    return caracteres
            