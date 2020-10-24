def total_do_semestre_por_bairro(dic):
    dic2 = {}
    for i in dic:
        for t in dic[i].values():
            total = sum(t[:5])
        dic2[i] = total 
        
    return dic2
        