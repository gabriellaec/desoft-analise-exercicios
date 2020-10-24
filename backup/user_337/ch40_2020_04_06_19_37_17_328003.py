'''def soma_valores (valores):
    soma = 0
    indice = 0
    while indice < len(valores):
        soma = soma + valores [indice]
        indice = indice + 1
    return soma'''

def soma_valores(valores):
    soma = 0
    for i in valores:
        soma += valores[i]
        print(soma)
    return soma