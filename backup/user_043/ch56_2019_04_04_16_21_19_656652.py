def calcula_total_da_nota(precos,quantidade):
    i=0
    soma=0
    while i<len(precos):
        soma+=precos[i]*quantidade[i]
        i+=1
    return soma