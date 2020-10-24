def total_do_semestre_por_bairro(x):
    dic = {}
    for key, values in x.items():
        i = 0
        d = 0
        g = 0
        if g <= 6:
            for i in values:
                d = i + d
        dic[key] = d
    return dic