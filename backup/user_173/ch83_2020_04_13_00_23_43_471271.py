def media_por_inicial (dic1):
    dic2 = {}
    media = 0
    for x in dic1:
        inicial = x[0]
        if inicial not in dic2:
            dic2[inicial] = dic1[x]
        else:
            dic2[inicial] = (dic2[inicial] + dic1[x])/2
    return dic2