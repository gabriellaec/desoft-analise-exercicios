def estritamente_crescente(lista):
    crescente=[]
    if lista==[]:
        crescente=crescente
    else:
        crescente.append(lista[0])
    i=1
    x=0
    while i<len(lista):
        while lista[x]<lista[i]:
            x+=1
        if x==i:
            crescente.append(lista[i])
        i+=1
    return crescente