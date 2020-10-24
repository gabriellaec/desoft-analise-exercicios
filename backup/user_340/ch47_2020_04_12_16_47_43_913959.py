def estritamente_crescente(lista):
    lista1=[]
    if len(lista)>0:
        lista1=[lista[0]]
    else: return lista1
    i=1
    a=0
    while i<len(lista):
        if lista[i]>lista1[a]:
            lista1.append(lista[i])
            a+=1
        i+=1
    return lista1