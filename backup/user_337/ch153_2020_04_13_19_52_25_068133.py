def agrupa_por_idade(nome_idade):
    faixa = {}
    lista_c = []
    lista_ado = []
    lista_ad = []
    lista_i = []
    for i in nome_idade:
        if nome_idade[i] <= 11:
            lista_c.append(i)
        elif nome_idade[i] >= 12 and nome_idade[i] <= 17:
            lista_ado.append(i)
        elif nome_idade[i] >= 18 and nome_idade[i] <= 59:
            lista_ad.append(i)
        else:
            lista_i.append(i)
    faixa['criança'] = lista_c
    faixa['adolescente'] = lista_ado
    faixa['adulto'] = lista_ad
    faixa['idoso'] = lista_i
    return faixa
            