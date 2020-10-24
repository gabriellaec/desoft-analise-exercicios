def aniversariantes_de_setembro (dic):
    dic_set = {}
    for k in dic.keys():
        v = dic[k]
        if v[3:5] == '09':
            dic_set[k] = v
    return dic_set