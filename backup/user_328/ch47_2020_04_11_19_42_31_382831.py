def estritamente_crescente(lista):
    if len(lista)==0:
        return lista
    i=0
    c=0
    x= (len(lista)-1)
    lista2= [0]
    lista2[0]= lista[0]
    while x != i:
        if lista[i] > lista2[c]:
            lista2.insert(i, lista[i])
            i += 1
            c += 1
        else:
            i += 1
    return lista2