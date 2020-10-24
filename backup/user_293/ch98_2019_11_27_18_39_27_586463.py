def bairro_mais_custoso(dic):
    maior_gasto = dict()
    for e in total_do_semestre_por_bairro:
        custo_maior = 0
        for i in total_do_semestre_por_bairro[e]:
            bairro_total = total_do_semestre_por_bairro[e]
            maior_gasto[e] = bairro_total
            if custo_maior < maior_gasto[e]:
                custo_maior = maior_gasto[e]
    return maior_gasto[e]