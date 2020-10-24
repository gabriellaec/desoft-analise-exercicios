def calcula_total_da_nota(lista1, lista2):
    preco_total = 0
    i = 0
    while i < len(lista1):
        preco_prod = lista1[i]*lista2[i]
        preco_total = preco_total + preco_prod
        i += 1
    return preco_total