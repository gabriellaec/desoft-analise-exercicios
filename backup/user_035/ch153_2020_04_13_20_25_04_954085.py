def agrupa_por_idade(dic):
    lista_idades = list(dic.values())
    lista_nomes = list(dic.keys())
    novo_dic = {}
    lista_crianca = []
    lista_adolescente = []
    lista_adulto = []
    lista_idoso = []
    for e in lista_idades:
        if e <= 11:
            lista_crianca.append(lista_nomes[lista_idades.index])
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