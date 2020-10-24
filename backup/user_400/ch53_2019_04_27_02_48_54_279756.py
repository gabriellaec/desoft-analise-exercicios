def inverte_lista(x):
    i = 0
    lista = []
    tamanho = len(x)
    while i < tamanho:
        lista.append(x[-1])
        del x[-1]
        i += 1
    
    return lista
        