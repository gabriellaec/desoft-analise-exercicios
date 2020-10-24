def agrupa_por_idade(d):
    dic = {}
    c = []
    a = []
    ad = []
    ido = []
    for n, i in d.items():
        if i <= 11:
            c.append(n)
        if 12 <= i <=17:
            a.append(n)
        if 18 <= i <= 59:
            ad.append(n)
        if i >= 60:
            ido.append(n)
    dic['criança'] = c
    dic['adolescente'] = a
    dic['adulto'] = ad
    dic['idoso'] = ido
    return dic
