def total_do_semestre_por_bairro(dic):
    d = {}
    for each in dic:
         d[each] = sum(dic[each][-6:])
    return d

def bairro_mais_custoso(dic):
    dic = total_do_semestre_por_bairro(dic)
    return list({k: v for k, v in sorted(dic.items(), key=lambda item: item[1])})[-1]