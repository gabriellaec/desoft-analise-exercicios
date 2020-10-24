'''def soma_valores (valores):
    soma = 0
    indice = 0
    while indice < len(valores):
        soma = soma + valores [indice]
        indice = indice + 1
    return soma'''

def soma_valores(valores):
    for i in valores:
        soma = soma + valores[i]
    return soma