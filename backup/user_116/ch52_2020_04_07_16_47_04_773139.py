def calcula_total_da_nota(preco,quant):
    lista3=[]
    for x in zip(preco,quant):
        lista3.append(x[0]*x[1])
    return lista3