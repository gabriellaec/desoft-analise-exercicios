def estritamente_crescente(lista):
    cresce=[]
    i=0
    while i < len(lista):
        n=lista[i]
        if lista[i-1]<n:
            cresce.append(n)
            i+=1
    return cresce
       