def calcula_total_da_nota(preco,quantidade):
    n=0
    total=0
    while n<len(preco) and n<len(quantidade):
        total=quantidade[n]*preco[n]+total
        n+=1
    return total
