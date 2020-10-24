def lista_sufixos(n):
    lista1 = list(n)
    tamanho = len(n)
    lista2 = [] 
    i =  tamanho -1
    while i > 0:
        del(lista1[0])
        x = ' '.join(lista1)
        lista2.append(x)
        i = i -1
    return lista2