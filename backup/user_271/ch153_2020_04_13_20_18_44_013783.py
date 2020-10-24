def agrupa_por_idade(dicionario1):
    dicionario2={}
    for nome, idade in dicionario1.items():
        if idade<=11:
            dicionario2['criança']+=nome
        if 12<=idade<=17:
            dicionario2['adolescente']+=nome
        if 18<=idade<=59:
            dicionario2['adulto']+=nome
        else:
            dicionario2['idoso']+=nome
    return dicionario2