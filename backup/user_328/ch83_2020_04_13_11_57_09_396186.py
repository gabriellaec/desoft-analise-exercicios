def medias_por_inicial(lista):
    dict2= {}
    dict= {}
    dict2['conta'] = 1
    for k,v in lista.items():
        x = k
        y = v
        if x[0] not in dict:
            dict[x[0]] = y
        else:
            dict2['conta'] += 1
            dict[x[0]] = dict[x[0]] + y
    for i in dict.keys():
        if dict[i] > 10:
            dict[i] = dict[i]/dict2['conta']
    return dict