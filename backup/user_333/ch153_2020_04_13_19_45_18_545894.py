def agrupa_por_idade(dicionario):
    grupo_idade={'criança':[],'adolescente':[],'adulto':[],'idoso':[]}
    for nome_e_idade in dicionario.items():
        nome=nome_e_idade[0]
        idade=nome_e_idade[1]
        if idade<=11:
            grupo_idade['criança'].append(nome)
        elif 12<=idade<=17:
            grupo_idade['adolescente'].append(nome)
        elif 18<=idade<=59:
            grupo_idade['adulto'].append(nome)
        else:
            grupo_idade['idoso'].append(nome)
    return grupo_idade
            