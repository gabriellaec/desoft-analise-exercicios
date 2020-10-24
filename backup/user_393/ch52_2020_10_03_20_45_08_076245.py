def calcula_total_da_nota(preco,quantidade):
    lista_total= []
    i= 0
    while i < len(preco):
        lista_total.append(preco[i]*quantidade[i])
        i= i + 1
    x= 0 
    preco_total=0
    while x < len(lista_total):
        preco_total= preco_total + lista_total[x]
        x= x + 1
    return preco_total
