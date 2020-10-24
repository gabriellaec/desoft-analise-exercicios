def agrupa_por_idade(x):
    agrup={'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for k,v in x.items():
        if v <=11:
            agrup['criança'].append(k)
        if v >11 and v<=17:
            agrup['adolescente'].append(k)
        if v >17 and v<=59:
            agrup['adulto'].append(k)
        if v >59:
            agrup['idoso'].append(k)
    return agrup