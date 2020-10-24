def estritamente_crescente(lista):
    i=1
    cresce=[]
    if len(lista)>0:
        maior=lista[0]
        cresce.append(maior)
        while i<len(lista):
            if lista[i]>maior:
                cresce.append(lista[i])
                maior=lista[i]
            i+=1
        return cresce
    else:
        return cresce