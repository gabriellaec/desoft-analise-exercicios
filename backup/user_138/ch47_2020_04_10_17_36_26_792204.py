def estritamente_crescente(lista):
    listaB=[]
    if len(lista)>0:
        listaB=lista[0]
    else: return listaB
    i=1
    a=0
    while i<len(lista):
        if lista[i]>listaB[a]:
            listaB.append(lista[i])
            a+=1
        i+=1
    return listaB