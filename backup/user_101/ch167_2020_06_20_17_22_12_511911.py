def total_do_semestre_por_bairro(d):
    dic = {}
    for e in d.items():
        dic[e[0]] = sum(e[1][6:])
    return dic

def bairro_mais_custoso(dic):
    maior_gasto = 0
    for d in total_do_semestre_por_bairro(dic).items():
        if int(sum(d[1])) > maior_gasto:
            maior_gasto = sum(d[1])
            bairro = d[0]
        maior_gasto = 0
    return bairro