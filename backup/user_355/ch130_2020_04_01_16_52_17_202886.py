def monta_mala (lista1):
    lista3= []
    i=0
    j=1
    while i<len(lista1):
        a=lista1[i]
        b=lista1[j]
        c=soma [a,b]
        if c<23:
            lista3.append(a)
            lista3.append(b)
        i+=1
        j+=1
    return lista3