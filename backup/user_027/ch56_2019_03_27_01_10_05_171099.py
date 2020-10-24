def calcula_total_da_nota(x,y):
    soma = 0
    for i in range(len(x)):
        soma += float(x[i])*int(y[i])
    return soma