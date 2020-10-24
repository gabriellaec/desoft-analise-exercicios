def total_do_semestre_por_bairro(dic):
    newdic = {}
    for k,v in dic.items():
        for i in range(7):
            newdic[k] = []
            newdic[k].append(i)
    return newdic