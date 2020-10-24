def quantos_uns(x):
    soma = 0
    indice = 0
    while indice < len(x):
        if x[indice] == '1':
           soma = soma + 1
           indice += 1
        else:
            indice += 1
    return soma


