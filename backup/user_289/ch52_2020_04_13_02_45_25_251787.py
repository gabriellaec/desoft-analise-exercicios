def calcula_total_da_nota(lista_preço, lista_qntd):
    i = 0
    valor_total = 0
    while i < len(lista_qntd):
        valor = lista_preço[i]*lista_qntd[i]
        valor_total += valor
        i += 1