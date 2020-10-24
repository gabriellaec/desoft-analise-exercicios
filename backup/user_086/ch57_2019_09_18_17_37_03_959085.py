def soma_impares(numeros):
    contador=0
    soma=0
    while contador<len(numeros):
        n=1
        while n<numeros[(len(numeros)-1)]:
            if numeros[contador]==n:
                soma=soma+n
            n+=2
        contador+=1
    return soma