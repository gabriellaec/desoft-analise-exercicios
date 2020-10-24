def soma_impares(n):
    i = 0
    lista_impares = []
    while i < len(n):
        if n[i] % 2 != 0:
            lista_impares.append(n[i])
        i += 1
    soma = 0 
    contador = 0
    while contador < len(lista_impares):
        soma += lista_impares[0]
        contador += 1
    return soma 
        