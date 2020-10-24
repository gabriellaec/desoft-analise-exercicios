def lista_sufixos(n):
    lista1 = list(n)
    tamanho = len(n)
    lista2 = [] 
    i =  0
    while i < tamanho:
        x = ' '.join(lista1)
        lista2.append(x)
        del(lista1[0])
        i = i + 1
    return lista2