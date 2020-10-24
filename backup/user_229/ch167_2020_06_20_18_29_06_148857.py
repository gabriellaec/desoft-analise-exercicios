def total_do_semestre_por_bairro(gastos_infraestrutura):
    gasto_total = {}
    for bairro, custos_lista in gastos_infraestrutura.items():
        total = 0
        for i in range(6, 12):
            valor = custos_lista[i]
            total += valor
        gasto_total[bairro] = total
    return gasto_total

def bairro_mais_custoso(total_do_semestre_por_bairro(gastos_infraestrutura)):
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