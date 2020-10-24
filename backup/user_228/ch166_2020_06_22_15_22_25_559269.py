def total_do_semestre_por_bairro(empresa):
    semestral={}
    soma=0
    for bairro in empresa:
        for gasto in empresa[bairro][6:]:
            soma+=empresa[bairro][6:]
            semestral[bairro]=soma
    return semestral
            
    