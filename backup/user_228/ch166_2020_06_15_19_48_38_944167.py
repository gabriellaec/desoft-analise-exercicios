def total_do_semestre_por_bairro(empresa):
    dic={}
    for bairro in empresa:
        dic[bairro]=0
        for gasto in empresa[bairro][6:]:
            dic[bairro]+=gasto
    return dic
            
            
    