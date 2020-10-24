def bairro_mais_custoso(gastos_infraestrutura):
    maior_bairro = ''
    maior_valor = 0
    for bairro, custos_lista in gastos_infraestrutura.items():
        valor = 0
        for custo in custos_lista:
            valor += custo
        if valor > maior_valor:
            maior_bairro = bairro
            maior_valor = valor
    return maior_bairro