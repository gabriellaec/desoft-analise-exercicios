def verifica_numero(x):
    i = 0
    soma = 0
    while i < len(x):
        soma += int(x[i]) ** int(x[i])
        i += 1

    if soma == int(x):
        return True
    else:
        return False