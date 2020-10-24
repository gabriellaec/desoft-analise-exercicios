def calcula_total_da_nota(x,y):
    z=0
    i=0
    while i<len(x):
        z=z+x[i]*y[i]
        i+=1
    return z
        