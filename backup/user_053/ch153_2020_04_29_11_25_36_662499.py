# Aluno: Jamesson Leandro Paiva Santos
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
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    dict_agrupamento = {'criança': lista1, 'adolescente': lista2, 'adulto': lista3, 'idoso': lista4}
    for nome, idade in dict_nome_idade.items():
        for classificacao, listas in dict_agrupamento.items():
                if classifica_idade(idade) == classificacao:
                    listas.append(nome)                    
    return dict_agrupamento