def aniversariantes_de_setembro(dicio):
    nv_dicio = {}
    k = dicio.keys()
    v = dicio.values()
    for k,v in dicio.items():
        nv_dicio[k] = v[6:]
    return nv_dicio
        