def calcula_total_da_nota(lista1, lista2):
    preco = 0
    i = 0
    while i<len(lista1):
        preco+=(lista1[i]*lista2[i])
    return preco