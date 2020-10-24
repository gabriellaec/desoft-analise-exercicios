def mais_populoso(estados):
    r = 0
    estado = ''
    for estado, carac in estados.items():
        for key in carac:
            if r < carac[key]:
                r = carac[key]
                estado = key
    result = "O estado mais populoso é {0} com {1} habitantes.".format(estado, r)
    return result