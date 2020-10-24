def total_do_semestre_por_bairro(dict):
    dict2 = {}
    for key in dict:
        gasto = 0
        lista = dict[key][6:]
        for i in lista:
            gasto += float(i)
        dict2[key] = gasto
    return dict2

def bairro_mais_custoso(total):
    dict_total = total_do_semestre_por_bairro(total)
    maiscaro = ''
    max = 0
    for bairro in dict_total:
        if dict_total[bairro] > max:
            max = dict_total[bairro]
            maiscaro = bairro
    return maiscaro