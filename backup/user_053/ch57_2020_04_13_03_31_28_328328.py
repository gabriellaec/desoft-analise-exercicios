def verifica_progressao(n):
    i = 0
    a = (n[i]-n[i+1])
    b = (n[i]/n[i+1])
    while (i+2) < len(n):
        if a == (n[i + 1] - n[i + 2]) and b == (n[i + 1]/n[i + 2]):
            resultado = 'AG'
        elif a == (n[i + 1] - n[i + 2]):
            resultado = 'PA'
        elif b == (n[i + 1]/n[i + 2]):
            resultado = 'PG'
        else:
            resultado = 'NA'
        i += 1
    return resultado