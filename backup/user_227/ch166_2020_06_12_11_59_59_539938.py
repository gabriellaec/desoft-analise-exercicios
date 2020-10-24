def total_do_semestre_por_bairro(dic):
    novo_dic = {}
    for bairro in dic:
        novo_dic[bairro] = sum(dic[bairro][6:])
    
    return novo_dic