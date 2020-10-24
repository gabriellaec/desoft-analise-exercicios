def lista_sufixos (texto):
    lista = [texto]
    i = 1
    while i < len(texto):
        a = texto - texto[i] - texto[i-1]
        lista.append(a)
        i += 1
    return a
        