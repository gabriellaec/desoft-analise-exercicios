def total_do_semestre_por_bairro(dic):
    for bairro, gastos in dic.items():
        dic[bairro] = sum(gastos[6:12])
    return dic


def bairro_mais_custoso(dic):
    total_do_semestre_por_bairro(dic)
    
    bairros = []
    custos = []
    for bairro, custo in dic.items():
        bairros.append(bairro)
        custos.append(custo)
    return bairros[custos.index(max(custos))]