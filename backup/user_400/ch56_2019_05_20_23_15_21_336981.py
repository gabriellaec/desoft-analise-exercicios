def calcula_total_da_nota(x,y):
    soma = 0
    for i in range(0, len(x)):
        soma += x[i]*y[i]
    return soma