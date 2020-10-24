def soma_impares(lista):
    i=0
    soma=0
    while i < len(lista):
        if lista[i]%2 == 0:
            soma = soma 
        else:
            soma +=1
        i+=1
    return soma 
            