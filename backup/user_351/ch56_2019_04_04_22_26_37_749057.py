def calcula_total_da_nota(produtos,quantidades):
    nota=0
    i=0
    while i<len(produtos) and i <len(quantidades):
        nota+=produtos[i]*quantidades[i]
    i+=1
    return nota