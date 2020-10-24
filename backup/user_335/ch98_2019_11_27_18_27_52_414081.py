def bairro_mais_custoso(gastos_infra):
    gasto_6meses = total_do_semestre_por_bairro(gastos_infra)
    b_mais_custoso_gasto = 0 #Nome do bairro
    b_mais_custoso = 0 #Valor para o gasto do bairro

    for bairro in gasto_6meses:
        gasto = gasto_6meses[bairro]

        if gasto > b_mais_custoso_gasto:
            b_mais_custoso = bairro
            b_mais_custoso_gasto = gasto

    return b_mais_custoso