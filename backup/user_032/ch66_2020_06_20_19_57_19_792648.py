def lista_sufixos(palavra):
    lista = []
    i = 0
    for s in palavra:
        word = palavra[i:]
        lista.append(word)
        i += 1
    return lista