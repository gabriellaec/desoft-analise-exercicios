def total_do_semestre_por_bairro(dicio):
    for l,m in dicio.items():
        dicio[l]=sum(m[6:12])
    return dicio