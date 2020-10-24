def total_do_semestre_por_bairro(dg):
    ds = {}
    soma = 0

    for k, v in dg.items():
        v2 = v[6:12]
        for i in v2:
            soma += i            
            
        ds[k] = soma
        
    return ds