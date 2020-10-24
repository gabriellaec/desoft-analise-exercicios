def estritamente_crescente(lista):
    lista2=[]
    v=0
    for i in lista:
        if i>v:
            v=i
            lista2.append(v)
    return lista2
                                         