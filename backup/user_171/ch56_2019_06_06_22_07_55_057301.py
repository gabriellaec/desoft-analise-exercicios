def calcula_total_da_nota(precos, quantidades):
    nota_fiscal=0
    for p in range(len(precos)): 
        t=precos[p]*quantidades[p]
        nota_fiscal+=t
    return nota_fiscal