def quantos_uns(x):
    i = 0
    soma = 0
    while i in x:
        if i == 1:
            soma += i
        else:
            break
        i += 1
    return soma
