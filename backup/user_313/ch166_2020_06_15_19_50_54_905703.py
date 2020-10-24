def total_do_semestre_por_bairro(d1):
    soma = 0
    bairros = dict()
    
    for k,v in d1.items():
        for i in v[6:]:
            soma += i
        
        
        bairros[k] = soma
            
    return bairros