def total_do_semestre_por_bairro(dici):
    
    dici_ = {}
    
    for k,v in dici.items():
        soma = 0
        i = 5
        while i < len(v):
            soma = soma + v[i]
            i+=1
            
        dici_[k] = soma
        
    return dici_