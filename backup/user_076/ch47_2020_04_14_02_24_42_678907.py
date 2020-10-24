def estritamente_crescente (lista):
    crescente = []
    i = 0
    if len(lista)>0:
        crescente.append(lista[0])
    while i+1<len(lista):
        if lista[i+1]>lista[i]:
            crescente.append(lista[i+1])
        i+=1
    return crescente