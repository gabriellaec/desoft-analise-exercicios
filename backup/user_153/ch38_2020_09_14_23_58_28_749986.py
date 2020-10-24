def quantos_uns(n):
    n_str = str(n)
    soma = 0
    for alg in n_str:
        if alg == '1':
            soma += 1
    return soma

