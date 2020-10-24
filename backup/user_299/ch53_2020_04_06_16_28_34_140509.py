def soma_impares (lista):
    soma=0.0
    for e in lista:
        if e%2==0:
            del e
        else:
            soma=soma+e
    return soma