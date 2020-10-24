def mais_populoso (dic_estados):
    
    mais_populoso = ''
    maior_população = 0
    
    for estado, municipios in dic_estados.items():
        totals = 0
        for valor in municipios.values():
            totals += valor
            
        if totals > maior_população:
            maior_população = totals
            mais_populoso = estado 
            
    return mais_populoso
        