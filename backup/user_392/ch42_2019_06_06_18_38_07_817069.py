def quantos_uns(x):
    numero = str(x)
    soma = 0
    for algarismo in numero:
        if algarismo == '1':
            soma += 1
    return soma

       
        