def calcula_total_da_nota(preço, quantidade):
    i = 0
    while i < len(preço):
        nota_fiscal= preço[i]*quantidade[i]
        i+=1
        return nota_fiscal