def agrupa_por_idade(dicionario):
    novo_dicionario=dict()
    for k in dicionario.items():
        if dicionario[k]<=11:
            novo_dicionario["criança"]+=k
        elif dicionario[k]>=12 and dicionario[k]<=17:
            novo_dicionario["adolescente"]+=k
        elif dicionario[k]>=18 and dicionario[k]<=59:
            novo_dicionario["adulto"]+=k
        else:
            novo_dicionario["idoso"]+=k
    return novo_dicionario