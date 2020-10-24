def soma_valores(n):
    soma = 0
    i = 0
    tamanho = len(n)
    while i < tamanho:
        soma = soma + n[i]
        i = i + 1
    return soma


