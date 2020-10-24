def lista_sufixos (texto):
    lista = []
    i = 0
    while i < len(texto):
        a = texto - texto[i]
        lista.append(a)
        i += 1
    return a
        