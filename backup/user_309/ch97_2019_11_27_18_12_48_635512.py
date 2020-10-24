def total_do_semestre_por_bairro(dic):
    gasto_total = dict()
    k = dic.keys()
    v = sum([ int(v) for v[:7] in dic.values() ])
    gasto_total[k] = v 
    return gasto_total
        
