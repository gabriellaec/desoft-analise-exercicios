def total_do_semestre_por_bairro(x):
    total = dict()
    for bairro, gasto in x.items():
        f = x[bairro][0:6]
        s = sum(f)
        total[bairro] = s    
    return total
    
        
        
    