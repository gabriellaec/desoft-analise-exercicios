def classifica_idade(idade):
    if idade <= 11:
        return 'criança'
    elif idade >= 12 and idade <= 17:
        return 'adolescente'
    elif idade >= 18 and idade <= 59:
        return 'adulto'
    else:
        return 'idoso'



def agrupa_por_idade(dict_nome_idade):
    dict_agrupamento = {'criança': [],'adolescente': [], 'adulto': [], 'idoso': []}
    for nome, idade in dict_nome_idade.items():
        for classificacao, listas in dict_agrupamento.items():
                if classifica_idade(idade) == classificacao:
                    lista_nomes.append(nome)
    return dict_agrupamento