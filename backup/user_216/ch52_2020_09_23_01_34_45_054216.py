def calcula_total_da_nota(precos,quantidade):
    conta = 0
    i = 0
    while i < len(precos):
        conta = conta + precos[i] * quantidade[i]
        i += 1
    return conta