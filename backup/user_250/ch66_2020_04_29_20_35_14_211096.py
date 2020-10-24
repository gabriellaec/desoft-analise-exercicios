def lista_sufixos(palavra):
    lista = []
    i = 1
    while i < len(palavra)-1:
        lista.append(palavra[i+1:])
        i += 1
    return lista