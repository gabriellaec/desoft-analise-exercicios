def calcula_total_da_nota(x,y):
    preço = []
    i = 0
    while i < len(x):
        preço.append(x[i]*y[i])
        i = i + 1
    preço = sum(preço)
    return preço
        
    