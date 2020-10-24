def interseccao_chaves(x,y):
    lista = []
    for chaves in x.keys():
        lista.append(chaves)
    for chaves2 in y.keys():
        lista.append(chaves2)
    
    return(lista)