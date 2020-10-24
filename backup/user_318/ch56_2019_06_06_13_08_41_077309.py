def calcula_total_da_nota(preco,quantidade):
    valor=0
    i=0
    while i<len(preco):
        valor+=preco[i]*quantidade[i]
        i+=1
    return valor