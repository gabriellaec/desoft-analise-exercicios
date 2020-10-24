def calcula_total_da_nota(lista_precos, lista_qtd):
    i = 0
    total = 0
    while (i < len(lista_precos)):
        total = total + ( lista_precos[i]*lista_qtd[i])
        i = i + 1
    return total