def total_do_semestre_por_bairro(dic):
    d = []
    for each in dic:
         d[each] = sum(dic[each][-6:])
    print(d)
    return d