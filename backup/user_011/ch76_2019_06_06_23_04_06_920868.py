def aniversariantes_de_setembro(dicio):
    nv_dicio = {}
    k = dicio.keys()
    v = dicio.values()
    for k,v in dicio:
        nv_dicio[k] = dicio[k,v]
    return nv_dicio
        