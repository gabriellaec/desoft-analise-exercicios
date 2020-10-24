def total_do_semestre_por_bairro (dic):
    
    dic_totais = {}
    for k, v in dic.items():
        total = 0
        lista = v
        for gasto in v[:7]:
            total += gasto
            
        dic_totais[k] = total
        
    return dic_totais