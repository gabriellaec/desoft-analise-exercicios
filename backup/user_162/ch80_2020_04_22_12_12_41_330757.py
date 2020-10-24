def interseccao_chaves(d1, d2):
    lista1 = []
    lista2 = []
    lista = []
    
    for cahves in d1:
        lista1.append(cahves)
            
    for cahves in d2:
        lista2.append(cahves)
        for i in lista1:
            if i == lista2[-1]:
                lista.append(i)
    
    return lista
