def quantos_uns(x):
    soma = 0
    y = str(x)
    for i in y:
        if i == "1":
            soma += 1
    return soma
