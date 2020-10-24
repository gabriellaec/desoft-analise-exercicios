def total_do_semestre_por_bairro(dic):
    newdic = {}
    for k,v in dic.items():
            newdic[k] = 0
        for i in range(5):
            newdic[k] += v[i]
    return newdic