def total_do_semestre_por_bairro(dic):
    newdic = {}
    for k,v in dic.items():
        newdic[k] = 0
        for i in range(6,12):
            newdic[k] += v[i]
    return newdic