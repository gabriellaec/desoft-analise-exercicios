def encontra_maximo(ma):
    lista=[]
    for e in ma:
        for n in e:
           lista.append(n)
    for x in lista:     
        if n<0:
            n=-n
    return max(lista)