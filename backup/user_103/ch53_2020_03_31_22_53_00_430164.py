def soma_impares(lista):
    i=0
    while i<len(lista):
        if lista[i]%2==0:
            soma=0
            i+=1
        else:
            soma+=lista[i]
            return soma