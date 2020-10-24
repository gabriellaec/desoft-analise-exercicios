def estritamente_crescente(lista):
    i=0
    crescendo=[]
    crescendo.append(lista[i])
    while i+1<len(lista):
        if lista[i+1]-lista[i]>0:
            crescendo.append(lista[i+1])
        i+=1
    return crescendo