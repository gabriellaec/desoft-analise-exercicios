def total_do_semestre_por_bairro(dic):
    dic2 ={}
    for gastos in dic.values():
        dic2['Bairro 1'] = sum(dic['Bairro 1'])
        dic2['Bairro 2'] = sum(dic['Bairro 2'])
        dic2['Bairro 3'] = sum(dic['Bairro 3'])
    return dic2
