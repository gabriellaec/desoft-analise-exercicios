def total_do_semestre_por_bairro(d):
    dic = {}
    for e in d.items():
        dic[e[0]] = sum(e[1][5:])
    return dic