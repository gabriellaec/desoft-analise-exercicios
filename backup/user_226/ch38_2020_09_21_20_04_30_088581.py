def quantos_uns(numero):
    z = 0
    numeros = []
    numero = str(numero)
    while z < len(numero):
        numeros.append(numero[z])
        z += 1
    if '1' in numeros:
        i = 0
        repeticoes = []
        while i < len(numero):
            if numero[i] == '1':
                repeticoes.append(1)
            i += 1
        return len(repeticoes)
    else:
        return False
