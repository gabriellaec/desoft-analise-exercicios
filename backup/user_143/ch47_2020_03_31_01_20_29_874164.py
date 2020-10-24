def estritamente_crescente(lista):
    i=0
    c=1
    lista1=[]
    if len(lista) == 0:
        return lista1
    else:
        lista1.append(y)
        while c<=len(lista):
            y=lista[i]
            x=lista[c]
            if y<x:
                lista1.append(x)
                c+=1
                i+=1
            else:
                c+=1
    return lista1