def soma_impares(n):
    lista = [n]
    soma = 0
    for e in lista:
        if e%2!=0:
            soma = soma+e
    return soma
            
            