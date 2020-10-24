'''def soma_valores (valores):
    soma = 0
    indice = 0
    while indice < len(valores):
        soma = soma + valores [indice]
        indice = indice + 1
    return soma'''

def soma_valores(valores):
    soma = valores[0]
    print(valores)
    for i in valores:
        print(i)
        soma += valores[i+1]
    return soma