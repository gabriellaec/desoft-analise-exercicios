def agrupa_por_idade (dicionario):
    crianca = []
    adolescente = []
    adulta = []
    idoso = []
    if idades <= 11:
        crianca += dicionario.keys
    elif idades >= 12 and idades <= 17:
        adolescente += dicionario.keys
    elif idades >= 18 and idades <= 59:
        adulto += dicionario.keys
    else:
        idoso += dicionario.keys
    return dicionario
    
