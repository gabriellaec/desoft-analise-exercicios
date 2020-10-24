def agrupa_por_idade (dic):
    dic2 = {'crianca': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for nome, idade in dic.items():
        if idade <= 11:
            dic2 [crianca] = nome
        elif idade >= 12 and idade <=17:
            dic2 [adolescente] = nome
        elif idade >= 18 and idade <= 59:
            dic2 [adulto] = nome
        else:
            dic2 [idoso] = nome
        return dic2
