def soma_impares(lista):
    total=0
    for e in range (len(lista)):
        if lista[e]%2==1:
            total+=lista[e]    
    return total