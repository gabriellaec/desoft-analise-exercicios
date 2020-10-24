def agrupa_por_idade(dic):
    dicionario = {}
    dicionariofinal = {}
    for a in dic.keys():
        for b in dic.values():
            dicionario [a] = b
        for i in (len(dicionario)+1):
            if dicionario.values(i) <= 11:
                dicionariofinal[i] = "criança"
                dicionariofinal["criança"] = dicionario.keys()
            elif dicionario.values(i) >=12 and dicionario.values(i) <=17:
                dicionariofinal[i] = "adolescente"
                dicionariofinal["adolescente"] = dicionario.keys()
            elif dicionario.values(i) >=18 and dicionario.values(i) <=59:
                dicionariofinal[i] = "adulto"
                dicionariofinal["adulto"] = dicionario.keys()
            else:
                dicionariofinal[i] = "idoso"
                dicionariofinal["idoso"] = dicionario.keys()
    return dicionariofinal