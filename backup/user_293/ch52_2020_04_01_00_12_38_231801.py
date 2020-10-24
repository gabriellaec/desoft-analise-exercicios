def calcula_total_da_nota(lista_produtos,lista_quant):
    total = 0
    i = 0
    while i < len(lista_produtos):
        p = lista_produtos[i]
        q = lista_quant[i]
        total = total + p*q
        i += 1
    return total