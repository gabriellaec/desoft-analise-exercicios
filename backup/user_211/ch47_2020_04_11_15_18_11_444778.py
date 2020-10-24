def estritamente_crescente(lista):
    crescente=[]
    i=0
    while(i<len(lista)):
        if lista[i]>lista[i-1] and not lista[i] in crescente:
            crescente.append(lista[i])
        i+=1
    return crescente