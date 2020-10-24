def calcula_total_da_nota(precos, quantidades):
    i = 0
    total = 0
    while i < (len(precos)):
        total += (precos[i]*quantidades[i])
        i += 1
    print(total)