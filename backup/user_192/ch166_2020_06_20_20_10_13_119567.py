def total_do_semestre_por_bairro(x):
    total = dict()
    for bairro in x.keys():
        f = sum(x[bairro][0:6])
        total[bairro] = f  
    return total
    
        
        
    