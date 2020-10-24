def total_do_semestre_por_bairro(bairros):

    novo_dic = {}

    for bairro in bairros:

        total = 0
        lista_valores = bairros[bairro]

        for i in range(len(lista_valores)):

            if i > 5:
                total += lista_valores[i]

        novo_dic[bairro] = total

    return novo_dic

def bairro_mais_custoso(bairros):

    dic_custos = total_do_semestre_por_bairro(bairros)
    total = 0

    for custo in dic_custos.values():

        if custo > total:
            total = custo

    return total