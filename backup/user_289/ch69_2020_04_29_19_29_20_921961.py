def junta_listas(lista):
    nova_lista = []
    for e in lista:
        i = 0
        while i <= len(e): 
            X = e[i]
            nova_lista.append(X)
            i += 1
    return nova_lista