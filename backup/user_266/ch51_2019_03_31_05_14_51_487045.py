def estritamente_crescente(lista):
    i=1
    cresce=[]
    while i<len(lista):
        if lista[i]>lista[i-1]:
            cresce.append(lista[i])
        i+=1
    cresce.insert(0,lista[0])
    return cresce