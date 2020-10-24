def lista_sufixos(texto):
    lista = []
    i = 0
    for i in range(len(texto)):
        lista.append(texto[i:])

    return lista