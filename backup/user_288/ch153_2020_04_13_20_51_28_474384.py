def agrupa_por_idade (dicionario):
    crianca = []
    adolescente = []
    adulta = []
    idoso = []
    nomes = list(dicionario.keys())
    idades = list(dicionario.values())
    i = 1
    while i < len(dicionario):
        if idades[i] <= 11:
            crianca += nomes
        elif idades[i] >= 12 and idades[i] <= 17:
            adolescente += nomes
        elif idades[i] >= 18 and idades[i] <= 59:
            adulto += nomes
        else:
            idoso += nomes
        i += 1
        return dicionario
    
