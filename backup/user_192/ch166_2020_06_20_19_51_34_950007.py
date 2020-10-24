def total_do_semestre_por_bairro(x):
    total = dict()
    for bairro2, tot in total.items():
        for bairro, gasto in x.items():
            f = sum(x[bairro][0:6])
            total[bairro2] = f
    return total
    
        
        
    