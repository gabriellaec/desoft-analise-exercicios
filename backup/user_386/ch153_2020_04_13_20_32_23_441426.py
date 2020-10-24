def agrupa_por_idade(dicionario):
    grupo = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for a, b in dicionario.items():
        if b <= 11:
            grupo['criança'].append(a)
        elif b <= 17:
            grupo['adolescente'].append(a)
        elif b <= 59:
            grupo['adulto'].append(a)
        else:
            grupo['idoso'].append(a)
    return grupo