def agrupa_por_idade(dic):
    lista_idades = list(dic.values())
    novo_dic = {}
    for e in lista_idades:
        if e <= 11:
            novo_dic['criança'] = e
        elif e >= 12 and e <= 17:
            novo_dic['adolescente'] = e
        elif e >= 18 and e <= 59:
            novo_dic['adulto'] = e
        else:
            novo_dic['idoso'] = e
    return novo_dic        