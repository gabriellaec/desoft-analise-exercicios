def soma_valores(lista):
    i=0
    soma=1
    while i<len(lista):
        if lista[i]!=lista[0]:
            soma+=lista[i]
        i+=1
    return soma