def agrupa_por_idade (dic):
    dic2 = {}
    for nome, idade in dic.items():
        if idade <= 11:
            idade = criança
            dic2 [crianca] = nome
        elif idade >= 12 and idade <= 17:
            idade = adolescente
            dic2 [adolescente] = nome
        elif idade >= 18 and idade <= 59:
            idade = adulto
            dic2 [adulto] = nome
        else:
            idade = idoso
            dic2 [idoso] = nome
    return dic2

