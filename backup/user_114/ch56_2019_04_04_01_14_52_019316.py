def calcula_total_da_nota(x, y):
    i=0
    final=0
    while i<len(preco) and i<len(quantidade):
        total=x[i]*y[i]
        i=i+1
        final=final+total
    return final
