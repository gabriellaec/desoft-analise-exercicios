def agrupa_por_idade(dicionario):
    a = dict()
    a["criança"] = []
    a["adolescente"] = [ ]
    a["adulto"] = []
    a["idoso"] = []
    cri = []
    ado = []
    adu = []
    ido = []
    for nome in dicionario:
        if dicionario[nome] <= 11:
            cri.append(dicionario[nome])
        elif dicionario[nome] <= 17:
            ado.append(dicionario[nome])
        elif dicionario[nome] <= 59:
            adu.append(dicionario[nome])
        elif dicionario[nome] >= 60:
            ido.append(dicionario[nome])
    a["criança"] = cri
    a["adolescente"] = ado
    a["adulto"] = adu
    a["idoso"] = ido
    
    
    return a