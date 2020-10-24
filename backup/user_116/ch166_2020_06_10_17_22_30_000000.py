def total_do_semestre_por_bairro(dicio):
    for l,m in dicio.items():
        dicio[l]=sum(m[0:6])
    return dicio