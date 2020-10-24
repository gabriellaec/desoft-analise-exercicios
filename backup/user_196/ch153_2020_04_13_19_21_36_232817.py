def agrupa_por_idade(dic):
    dicionario = {}
    dicionariofinal = {}
    for a in dic.keys():
        for b in dic.values():
            dicionario [a] = b
    for i in (len(dicionario)+1):
        if dicionario.values(i) <= 11:
            dicionariofinal[i] = "criança"
        elif dicionario.values(i) >=12 and dicionario.values(i) <=17:
            dicionariofinal[i] = "adolescente"
        elif dicionario.values(i) >=18 and dicionario.values(i) <=59:
            dicionariofinal[i] = "adulto"
        else:
            dicionariofinal[i] = "idoso"
    return dicionariofinal