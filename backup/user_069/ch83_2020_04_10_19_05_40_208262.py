def medias_por_inicial (dic):
    dic_f = {}
    for k, v in dic.items():
        kf = k[:1]
        if not kf in dic_f.keys():
            dic_f[kf] = v
    return dic_f