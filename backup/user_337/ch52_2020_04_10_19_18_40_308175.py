def calcula_total_da_nota(preço, quantidade):
    i = 0
    while i<len(quantidade):
        total = total + (preço[i]*quantidade[i])
        i+=1
    return total