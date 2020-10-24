def total_do_semestre_por_bairro(dic):
    dic2 = {}
    for i in dic:
        total = sum(dic[i][:5])
        dic2[i] = total 
        
    return dic2
        