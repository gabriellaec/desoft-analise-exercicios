def lista_caracteres(palavra):
    i = 0
    caracteres = []
    while i < len(palavra):
        a = palavra[i]
        if not a in caracteres:
            caracteres.append(a)
        i += 1
    return caracteres
        