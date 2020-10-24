def total_do_semestre_por_bairro(bairros):

    novo_dic = {}

    for bairro in bairros:

        total = 0
        lista_valores = bairros[bairro]

        for valor in lista_valores:
            total += valor

        novo_dic[bairro] = total

    return novo_dic