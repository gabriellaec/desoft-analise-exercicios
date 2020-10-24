def calcula_total_da_nota(x, y):
    a = []
    for i in range(len(x)):
        for j in range(len(y)):
            z = x[i]*y[j]
            a.append(z)
    return sum(a)
            