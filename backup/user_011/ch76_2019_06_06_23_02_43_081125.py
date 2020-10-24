def aniversariantes_de_setembro(dicio):
    nv_dicio = {}
    k = dicio.keys()
    v = dicio.values()
    for k in dicio:
        nv_dicio[k] = str(v[5:])
    return nv_dicio
        