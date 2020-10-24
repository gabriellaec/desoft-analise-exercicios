def total_do_semestre_por_bairro(dic):
    novo = {}
    for bairro in dic:
        novo[bairro] = 0
        for mes in dic[bairro][6:]:
            novo[bairro]+= mes 
    return novo
            
            
    