def calcula_total_da_nota(lista_produtos,lista_quant):
    soma = 0
    i = 0
    for e in lista_produtos:
        x = e*lista_quant[i]
        soma += x
        i += 1
    return soma