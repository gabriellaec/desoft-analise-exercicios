def agrupa_por_idade(dicionario):
    novo_dicionario={}
    for i in dicionario:
        if i<=11:
            novo_dicionario[dicionario[i]]='criança'
        if i<=17:
            novo_dicionario[dicionario[i]]='adolescente'
        if i<=59:
            novo_dicionario[dicionario[i]]='adulto'
        else:
            novo_dicionario[dicionario[i]]='idoso'
        return novo_dicionario