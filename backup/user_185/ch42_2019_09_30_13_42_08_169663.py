def quantos_uns(número):
    numero = str(número)
    soma = 0
    i = 0
    while i < len(numero):
        if numero[i] == str(1):
            soma = soma + 1
        i = i + 1
    return soma