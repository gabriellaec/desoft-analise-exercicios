def agrupa_por_idade(dic):
    dicionariofinal = {'criança':[], 'adolescente':[], 'adulto': [], 'idoso': []}
    for k,v in dic.items():
        if v <= 11:
            dicionariofinal['criança'].append(k)
        elif 12 <= v <=17:
            dicionariofinal['adolescente'].append(k)
        elif 18 <= v <= 59:
            dicionariofinal['adulto'].append(k)
        elif v >= 60 :
            dicionariofinal['idoso'].append(k)
    return dicionariofinal