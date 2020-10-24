def soma_elementos (lista):
    soma = 0
    i = 0
    while i < len(lista):
        lista[i + 1] = lista[i]*(1/2)
        soma += lista[i]
        i += 1
    return soma