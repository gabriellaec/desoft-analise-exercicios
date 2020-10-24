def agrupa_por_idade (dic):
    dic_rev = {}
    lista_c = []
    lista_adl = []
    lista_adt = []
    lista_i = []

    for k, v in dic.items():

        if v <= 11:
            lista_c.append(k)

        elif v >= 12 and v <= 17:
            lista_adl.append(k)

        elif v >= 18 and v <= 59:
            lista_adt.append(k)

        else:
            lista_i.append(k)

    dic_rev['criança'] = lista_c
    dic_rev['adolescente'] = lista_adl
    dic_rev['adulto'] = lista_adt
    dic_rev['idoso'] = lista_i

    return dic_rev