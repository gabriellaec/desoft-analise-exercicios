def estritamente_crescente(lista):
    i=0
    c=1
    lista1=[]
    if len(lista) == 0:
        return lista1
    else:
        lista1.append(lista[i])
        while lista[i]<lista[c] and c<=len(lista):
            lista1.append(lista[c])
            c+=1
        c+=1
        return lista1