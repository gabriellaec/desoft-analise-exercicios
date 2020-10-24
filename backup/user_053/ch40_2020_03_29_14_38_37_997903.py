lista = [2,4,6,8,10]

def soma_valores(elementos):
    i=0
    soma=0
    while i < len(elementos):
        soma += elementos[i]
        i += 1
    return soma

print(soma_valores(lista))
        