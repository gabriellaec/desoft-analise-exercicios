def total_do_semestre_por_bairro (dic):
    
    
    for k, v in dic.items():
        total = 0
        lista = v
        for gasto in lista[:7]:
            total += gasto
            
        dic[k] = total