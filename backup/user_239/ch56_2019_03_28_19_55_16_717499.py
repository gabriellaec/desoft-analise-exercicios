def calcula_total_da_nota(x):
    i=0
    v=0
    while i<x[0][0]:
        v+=x[0][i]*x[1][i]
        i+=1
    return v