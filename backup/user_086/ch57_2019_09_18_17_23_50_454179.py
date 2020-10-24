def soma_impares(numeros):
    n=1
    contador=0
    soma=0
    while contador<len(numeros):
        if numeros[contador]==n:
            soma=soma+n
            n+=2
            contador+=1
        else:
            n+=2
    return soma