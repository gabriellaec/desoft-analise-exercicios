def estritamente_crescente(lista):
    i=0
    c=1
    lista1=[]
    while lista[i]<lista[c] and c<=len(lista):
        lista1.append(lista[c])
        lista1.append(lista[i])
        c+=1
    c+=1
    return lista1