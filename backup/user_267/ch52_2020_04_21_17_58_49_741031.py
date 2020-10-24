def calcula_total_da_nota(listap, listaq):
    i = 0
    total = 0
    while i < (len(listap)-1):
        preco = listap[i]*listaq[i]
        i += 1
        total += preco
    print(total)