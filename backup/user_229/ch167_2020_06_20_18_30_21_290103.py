def bairro_mais_custoso(gastos_infraestrutura):
    maior_bairro = ''
    maior_valor = 0
    for bairro, custos_lista in gastos_infraestrutura.items():
        valor = 0
        for i in range(6, 12):
            valor += custos_lista[i]
        if valor > maior_valor:
            maior_bairro = bairro
            maior_valor = valor
    return maior_bairro