def eh_crescente(x):
    maior = 0
    i = 0
    for k in x:
        if x[i] > maior:
            maior = x[i]
            i = i + 1
        else:
            return False
    return True