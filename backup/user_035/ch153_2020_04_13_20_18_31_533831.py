def agrupa_por_idade(dic):
    lista_idades = list(dic.values())
    novo_dic = {}
    for e in lista_idades:
        lista_crianca = []
        lista_adolescente = []
        lista_adulto = []
        lista_idoso = []
        if e <= 11:
            lista_crianca.append(e)
        elif e >= 12 and e <= 17:
            lista_adolescente.append(e)
        elif e >= 18 and e <= 59:
            lista_adulto.append(e)
        else:
            lista_idoso.append(e)

    novo_dic['criança'] = lista_crianca
    novo_dic['adolescente'] = lista_adolescente
    novo_dic['adulto'] = lista_adulto
    novo_dic['idoso'] = lista_idoso
    return novo_dic        