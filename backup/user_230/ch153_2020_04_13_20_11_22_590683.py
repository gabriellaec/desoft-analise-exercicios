def agrupa_por_idade(dicionario):
    novo_dicionario=dict()
    for k,i in dicionario.items():
        if i<=11:
            novo_dicionario["criança"]+=[k]
        elif i>=12 and i<=17:
            novo_dicionario["adolescente"]+=[k]
        elif i>=18 and i<=59:
            novo_dicionario["adulto"]+=[k]
        else:
            novo_dicionario["idoso"]+=[k]
    return novo_dicionario