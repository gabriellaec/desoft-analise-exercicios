def agrupa_por_idade(x):
    fet = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for k, v in x.items():
        if v <= 11:
            fet['criança'].append(k)
        if v <= 17:
            fet['adolescente'].append(k)
        if v <= 59:
            fet['adulto'].append(k)
        else:
            fet['idoso'].append(k)
    return(fet)
