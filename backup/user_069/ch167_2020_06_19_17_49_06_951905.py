def bairro_mais_custoso(bairros):

    dic_custos = total_do_semestre_por_bairro(bairros)
    total = 0

    for custo in dic_custos.values():

        if custo > total:
            total = custo

    return total