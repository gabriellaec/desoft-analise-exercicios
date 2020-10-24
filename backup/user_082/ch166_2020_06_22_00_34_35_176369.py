def total_do_semestre_por_bairro(empresa):
    novo_dic = {}

    for filial in empresa:
        novo_dic[filial] = 0

        for mes in empresa[filial][6:]:
            novo_dic[filial] += mes
    
    return novo_dic

