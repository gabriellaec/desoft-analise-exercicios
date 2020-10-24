def lista_caracteres(palavra):
    lista_letras = []
    t = 0
    while t < len(palavra):
        if palavra[t] not in lista_letras:
            lista_letras.append(palavra[t])
        t += 1
    return lista_letras