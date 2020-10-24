def encontra_maximo(ma):
    lista=[]
    for e in ma:
        for n in e:
            if n<0:
                n=-n
            lista.append(n)
    return max(lista)