def agrupa_por_idade (dic):
    dic_rev = {}

    for k, v in dic.items():
        vr = []
        vr.append(k)

        if v <= 11:
            if not vr in dic_rev.values():
                dic_rev['criança'] = vr
            else:
                dic_rev['criança'] += vr

        elif v >= 12 and v <= 17:
            if not vr in dic_rev.values():
                dic_rev['adolescente'] = vr
            else:
                dic_rev['adolescente'] += vr

        elif v >= 18 and v <= 59:
            if not vr in dic_rev.values():
                dic_rev['adulto'] = vr
            else:
                dic_rev['adulto'] += vr

        else:
            if not vr in dic_rev.values():
                dic_rev['idoso'] = vr
            else:
                dic_rev['idoso'] += vr
                
    return dic_rev