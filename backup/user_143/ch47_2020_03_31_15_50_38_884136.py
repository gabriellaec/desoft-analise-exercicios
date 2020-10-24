def estritamente_crescente(lista):
    i=0
    c=1
    lista1=[]
    if len(lista) == 0:
        return lista1
    else:
        j=lista[0]
        lista1.append(j)
        while c<=len(lista):
            y=lista[i]
            x=lista[c]
            if y<x:
                lista1.append(x)
                i=c
                c+=1
            else:
                c+=1
    return lista1