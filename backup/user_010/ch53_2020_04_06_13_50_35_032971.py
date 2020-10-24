numeros = [3, 9, 4, 6, 6]
def soma_impares (lista):
    s=0
    for e in lista:
        if e%2!=0:
            s+=e
    return s
print (soma_impares(numeros))