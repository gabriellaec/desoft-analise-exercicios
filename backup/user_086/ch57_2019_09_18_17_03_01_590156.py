def soma_impares(numeros):
    n=1
    contador=0
    soma=0
    while n<len(numeros):
        if numeros[contador]==n:
            soma+=n
        n+=2
        contador+=1
    return soma