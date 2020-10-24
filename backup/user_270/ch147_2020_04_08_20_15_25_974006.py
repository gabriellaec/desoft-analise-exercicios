def conta_ocorrencias(l):
    dic = {}
    for i in l:
        if not i in dic :
            dic[i] = 1
        else:
            dic[i] += 1
    return dic
def mais_frequente(l):
    new_l = conta_ocorrencias(l)
    k =[0,0]
    for i, g in new_l.items():
        if g > k[1]:
            k[1] = g
            k[0] = i
    return k[0]