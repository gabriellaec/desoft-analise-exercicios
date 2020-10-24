def calcula_total_da_nota(precos,quantidade):
    total=0
    i=0
    while i<len(precos):
        total+=precos[i]*quantidade[i]
        i+=1
    return total


   