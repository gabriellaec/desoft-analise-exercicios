def inverte_dicionario (dic):
    dic_rev = {}
    
    for k, v in dic.items():
        kr = v
        vr = []
        vr.append(k)
        if not kr in dic_rev:
            dic_rev[kr] = vr
        else:
            dic_rev[kr] += vr
    
    return dic_rev
