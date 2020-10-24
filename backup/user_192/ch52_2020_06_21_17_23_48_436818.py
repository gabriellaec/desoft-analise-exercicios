def calcula_total_da_nota(x, y):
    a = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] != 0 or y[j] != 0:
                z = x[i]*y[j]
                a.append(z)
            else:
                z = x[i]
                a.append(z)
    return sum(a)
            