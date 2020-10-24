def total_do_semestre_por_bairro(dic):
    newdic = {}
    for k,v in dic.items():
        newdic[k] = 0
        for i in range(6,11):
            newdic[k] += v[i]
    return newdic