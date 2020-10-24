def total_do_semestre_por_bairro(dic):
    dic2 = {'Bairro 1':[],'Bairro 2':[],'Bairro 3':[]}
    for bairros,gastos in dic.items():
        dic2['Bairro 1'].append(dic['Bairro 1'])
        dic2['Bairro 2'].append(dic['Bairro 2'])
        dic2['Bairro 3'].append(dic['Bairro 3'])
    return dic2