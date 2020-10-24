def calcula_total_da_nota(precos, quantidade):
    preco_total = 0
    i = 0

    while i < len(precos):
        valor = precos[i] * quantidade[i]
        preco_total+=valor
        i+=1

    return preco_total