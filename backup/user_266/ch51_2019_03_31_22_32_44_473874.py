def estritamente_crescente(lista):
    i=1
    maior=lista[0]
    cresce=[]
    cresce.append(maior)
    while i<len(lista):
        if lista[i]>maior:
            cresce.append(lista[i])
            maior=lista[i]
        i+=1
    return cresce