def medias_por_inicial (dic):
    dic_f = {}
    for k, v in dic.items():
        kf = k[:1]
        if not kf in dic_f.keys():
            dic_f[kf] = v
        else:
            for v2 in dic.values():
                if dic_f[kf] == v2 and v2 != v:
                    dic_f[kf] = (v + v2)/2
    return dic_f