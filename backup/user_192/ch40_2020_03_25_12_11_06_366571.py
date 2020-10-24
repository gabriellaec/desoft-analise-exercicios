
def soma_valores(n):
    n_elementos = len(n)
    i = 0
    soma = 0
    while i < n_elementos:
        soma += n[i]
        i += 1
        return soma
    