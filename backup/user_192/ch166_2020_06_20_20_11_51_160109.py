def total_do_semestre_por_bairro(x):
    total = dict()
    for bairro, gasto in x.items():
        total[bairro] = sum(x[bairro][0:6])
    return total
    
        
        
    