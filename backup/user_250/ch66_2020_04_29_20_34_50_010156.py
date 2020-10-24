def lista_sufixos(palavra):
    lista = []
    i = 1
    while i < len(palavra)-1:
        lista.append(palavra[i:])
        i += 1
    return lista