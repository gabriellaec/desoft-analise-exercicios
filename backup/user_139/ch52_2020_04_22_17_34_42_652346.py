def calcula_total_da_nota (x, y):
    soma = 0
    i = 0
    while i < len(x) and i < len(y):
        soma += x[i] * y[i]
        i +=1
    return soma