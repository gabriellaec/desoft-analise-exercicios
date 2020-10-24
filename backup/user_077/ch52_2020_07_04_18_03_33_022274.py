def calcula_total_da_nota(x,y):
    total=0
    for i in range(len(x)):
        total+=x[i]*y[i]
    return total