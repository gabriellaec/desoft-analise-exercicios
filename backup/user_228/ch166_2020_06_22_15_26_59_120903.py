def total_do_semestre_por_bairro(empresa):
    semestral={}
    for bairro in empresa:
        for gasto in empresa[bairro][6:]:
            semestral[bairro]+=gasto
    return semestral
            
    