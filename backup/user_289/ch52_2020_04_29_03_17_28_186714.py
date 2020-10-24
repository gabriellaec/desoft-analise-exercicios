def calcula_total_da_nota(lista_preco, lista_qntd):
    i = 0
    valor_total = 0
    for e in lista_preco:
        valor = e*lista_qntd[i]
        valor_total += valor
        i += 1
    return valor_total