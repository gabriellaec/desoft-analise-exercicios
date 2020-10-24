def total_do_semestre_por_bairro(dicionario):
    dicionario2 = {}
    for k in dicionario:
        for v in range(6, 12):
            if not k in dicionario2:
                dicionario2[k] = dicionario[k][v]
            else:
                dicionario2[k] += dicionario[k][v]
    return dicionario2

def bairro_mais_custoso(dic):
    dic2 = total_do_semestre_por_bairro(dic)
    for k, v in dic2.items():
        if v == max(dic2.values()):
            return k