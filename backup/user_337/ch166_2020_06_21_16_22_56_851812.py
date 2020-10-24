def total_do_semestre_por_bairro(dicionario):
    dic = {}
    for bairro in dicionario:
        gasto = 0
        lista = dicionario[bairro]
        for valor in lista[0:5]:
            gasto += valor
        dic[bairro] = gasto
    return dic
        