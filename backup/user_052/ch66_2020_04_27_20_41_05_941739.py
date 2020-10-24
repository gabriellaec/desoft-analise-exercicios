def lista_sufixos (texto):
    lista = [texto]
    i = 0
    while i < len(texto):
        a = texto[i:]
        lista.append(a)
        i += 1
    return lista
        