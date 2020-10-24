def calcula_total_da_nota (x,y):
    i = 0
    preço = 0
    while i<len(x):
        preço = preço + (x[i]*y[i])
        i+=1
    return preço
        