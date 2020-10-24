def estritamente_crescente(lista):
    i=0
    crescendo=[]
    crescendo.append(lista[i])
    maior=lista[i]
    while i<len(lista):
        if lista[i]>maior:
            crescendo.append(lista[i])
            maior=lista[i]
        i+=1
    return crescendo