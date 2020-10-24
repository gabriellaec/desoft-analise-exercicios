def lista_caracteres(palavra):
    lista = []
    for l in palavra:
        if l not in lista:
            lista.append(l)
    return lista
