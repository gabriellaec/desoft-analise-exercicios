def lista_caracteres(string):
    caracteres = []
    for c in string:
        if c not in caracteres:
            caracteres.append(c)
    return caracteres