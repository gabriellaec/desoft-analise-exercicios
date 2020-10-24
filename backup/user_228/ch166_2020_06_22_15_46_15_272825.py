def total_do_semestre_por_bairro(empresa):
    semestral={}
    for bairro in empresa:
        semestral[bairro]=0
        for gasto in empresa[bairro][6:]:
            semestral[bairro]+=gasto
    return semestral
            
    