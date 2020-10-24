lista = [1,2,3,4,5,6,7,8,9]

def soma_valores(x):
    soma = 0
    indice = 0
    while indice < len(x):
        soma = soma + x[indice]
        indice = indice + 1
    return soma

print (soma_valores(lista))