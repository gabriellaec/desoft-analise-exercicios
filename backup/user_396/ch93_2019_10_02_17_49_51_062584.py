def verifica_numero(x):
    k = str(x)
    i = 0
    soma = 0
    while i < len(k):
        soma += int(k[i]) ** int(k[i])
        i += 1

    if soma == int(k):
        return True
    else:
        return False