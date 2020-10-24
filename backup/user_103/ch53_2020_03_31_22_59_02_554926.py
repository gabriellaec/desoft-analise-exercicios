def soma_impares(lista):
    soma=0
    for i in range(len(lista)):
        if lista[i]%2!=0:
            soma+=lista[i]
            i+=1
        else:
            i+=1
        return soma
        
