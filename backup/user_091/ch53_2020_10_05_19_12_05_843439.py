

def soma_impares(numeros):
    soma=0
    for e in numeros:
        if e%2!=0:
            soma+=e
        else:
            soma+=0
    return soma