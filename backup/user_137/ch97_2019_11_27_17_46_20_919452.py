def total_do_semestre_por_bairro(d):
    r = dict()
    s = 0
    for key in d:
        for i in range(len(d[key]) - 6):
            s += float(d[key][i])
        r[key] = s
    return r