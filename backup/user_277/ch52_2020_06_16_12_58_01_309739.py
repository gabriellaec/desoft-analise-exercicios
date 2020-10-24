def calcula_total_da_nota(preco, quantidade):
    i=0
    k=0
    while i <len(preco):
        k=k+preco[i]*quantidade[i]
        i+=1
    return k