def eh_crescente(lista):
    i=0
    crescente = True
    while crescente == True and i<(len(lista)-1):
        if lista[i+1]<=lista[i]:
            crescente = False
        else:
            i+=1
    return crescente
print(eh_crescente([1,2,1,6]))