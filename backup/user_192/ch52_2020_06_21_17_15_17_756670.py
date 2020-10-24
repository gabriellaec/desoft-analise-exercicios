def calcula_total_da_nota(x, y):
    a= []
    for i in range(len(x)):
        for j in range(len(y)):
            a.append(x[i]*y[j])
    return sum(a)
            