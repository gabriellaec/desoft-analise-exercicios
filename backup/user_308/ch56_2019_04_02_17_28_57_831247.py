def calcula_total_da_nota(preço,quantidade):
    i=0
    total=0
    while i<len(preço):
        total+=preço[i]*quantidade[i]
        i+=1
    return total