
def soma_impares(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i]%2!=0:
            soma+=lista[i]
    return soma

def soma_impares(lista):
    soma = 0
    for i in lista:
        if i%2!=0:
            soma +=i
    return soma 