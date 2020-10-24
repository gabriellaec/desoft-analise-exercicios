def soma_valores(lista):
    soma = 0
    i = 0
    tamanho = len(lista)
    while i < tamanho:
        soma = soma + lista[i]
        i += 1
    return soma