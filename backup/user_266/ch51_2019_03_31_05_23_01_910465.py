def estritamente_crescente(lista):
    i=1
    cresce=[]
    while i<len(lista):
        if lista[i]>lista[i-1]:
            cresce.append(lista[i])
        i+=1
    i=1
    while i<len(cresce):
        if cresce[i]<=cresce[i-1]:
            del cresce[i]
        i+=1
    cresce.insert(0,lista[0])
    return cresce