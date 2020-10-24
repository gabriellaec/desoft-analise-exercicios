def bairro_mais_custoso(gastos):
    gastos2=total_do_semestre_por_bairro(gastos)
    maior_valor = list(gastos2.values())[0]
    bairro_custoso = list(gastos2.keys())[0]
    for bairro, valor in gastos2.items():
        if valor > maior_valor:
            bairro_custoso = bairro
            maior_valor = valor
    return bairro_custoso