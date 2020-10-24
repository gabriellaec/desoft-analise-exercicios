def agrupa_por_idade (pessoas, idade):
    dicionario = {}
    if idade < 11:
        dicionario[idade] = 'criança'
    elif 12 < idade < 17:
        dicionario[idade] = 'adolescente'
    elif 18 < idade < 59:
        dicionario[idade] = 'adulto'
    else:
        dicionario[idade] = 'idoso'
    
        