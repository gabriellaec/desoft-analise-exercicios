def agrupa_por_idade(dic_nome_idade):

    nomes_c = []
    nomes_ado = []
    nomes_adu = []
    nomes_i = []

    dic_faixa_nomes = {}

    for nome, idade in dic_nome_idade.items():
        if idade <= 11:
            nomes_c.append(nome)

        elif 12 <= idade <= 17:
            nomes_ado.append(nome)

        elif 17 <= idade <= 59:
            nomes_adu.append(nome)

        else:
            nomes_i.append(nome)

    dic_faixa_nomes['criança'] = nomes_c
    dic_faixa_nomes['adolescente'] = nomes_ado
    dic_faixa_nomes['adulto'] = nomes_adu
    dic_faixa_nomes['idoso'] = nomes_i

    return dic_faixa_nomes