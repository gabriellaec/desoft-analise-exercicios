def quantos_uns(x):
    x = str(x)
    i = 0
    soma = 0
    while i < len(x):
        if '1' == x[i]:
            soma = soma + 1
            i = i + 1
        else:
            i = i + 1    
    return soma