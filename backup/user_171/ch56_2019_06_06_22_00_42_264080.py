def calcula_total_da_nota(precos, quantidades):
    nota_fiscal=0
    for p in precos:
        for q in quantidades:
            t=p*q
        nota_fiscal+=t
    return nota_fiscal
        