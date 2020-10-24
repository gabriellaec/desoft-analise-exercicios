def quantos_uns(n):
    numero = str(n)
    i = 0
    quantos_1 = 0
    while i < len(numero):
        if numero[i] == '1':
            quantos_1 += 1
            i += 1
        else: 
            i += 1
    return (quantos_1)