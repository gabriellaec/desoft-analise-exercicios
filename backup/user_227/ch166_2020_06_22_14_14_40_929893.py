def total_do_semestre_por_bairro(dic):
    novo_dic = {}
    for bairro in dic:
        lista = dic[bairro][6:]
        novo_dic[bairro] = sum(lista)
     
    return novo_dic