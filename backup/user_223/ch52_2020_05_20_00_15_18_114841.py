def calcula_total_da_nota(preço, quantidade):
    total = 0
    i=0
    for i in range (len(preço)):
        total+= preço[i]*quantidade[i]
    return total