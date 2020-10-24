def total_do_semestre_por_bairro(dic):
    newdic = {}
    for k,v in dic.items():
        newdic[k] = 0
        for i in range(6,12):
            newdic[k] += v[i]
    return newdic
def bairro_mais_custoso(dic):
    sum = 0
    newdic1 = total_do_semestre_por_bairro(dic)
    bairro = 0
    for k,v in newdic1.items():
        if v > sum:
            bairro = k
            sum = v
    return bairro