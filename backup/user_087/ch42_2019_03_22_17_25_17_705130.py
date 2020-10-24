def quantos_uns(x):
    sx = str(x)
    soma = 0
    indice = 0
    while indice < len(sx):
        if sx[indice] == '1':
            soma = soma + 1
            indice += 1
        else:
            indice += 1
    return soma


