def agrupa_por_idade(dicionario):
    x = {'crianca':[],'adolescente':[],'adulto':[],'idoso':[]}
    keys = dicionario.key()
    for nome in keys:
        idade = dicionario[nome]
        if idade <= 11:
            x['crianca'].append(nome)
        elif 12 <= idade <= 17:
            x['adolescente'].append(nome)
        elif 18 <= idade <= 59:
            x['adulto'].append(nome)
        else:
            x['idoso'].append(nome)
    return x
                               
            