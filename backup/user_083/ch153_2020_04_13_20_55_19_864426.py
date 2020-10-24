def agrupa_por_idade(dicionario):
    criança=[]
    adolescente=[]
    adulto=[]
    idoso=[]
    novo_dicionario={'criança': criança, 'adolescente': adolescente, 'adulto': adulto, 'idoso': idoso}
    for g,i in dicionario.items:
        if i<=11:
            criança.append(g)
        if i<=17:
            adolescente.append(g)
        if i<=59:
            adulto.append(g)
        else:
            idoso.append(g)
        return novo_dicionario