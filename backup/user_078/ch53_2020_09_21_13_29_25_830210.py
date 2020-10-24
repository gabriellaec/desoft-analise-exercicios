
def soma_impares (lista):
    impares = []
    soma = 0

    for i in lista:
        
        if i % 2 != 0:
            impares.append(i)

    for j in impares:
        soma += j
    
    return soma