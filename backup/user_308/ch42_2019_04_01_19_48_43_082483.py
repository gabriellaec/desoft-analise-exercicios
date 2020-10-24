def quantos_uns(x):
    quant=0
    cont=0
    while cont<len(x):
        if x[cont]==1:
            quant+=1
            cont+=1
        else:
            cont+=1
    return quant