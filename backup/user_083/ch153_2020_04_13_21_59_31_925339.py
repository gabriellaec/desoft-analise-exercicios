def agrupa_por_idade(dicionario):
    criança=[]
    adolescente=[]
    adulto=[]
    idoso=[]
    novo_dicionario={'criança': criança, 'adolescente': adolescente, 'adulto': adulto, 'idoso': idoso}
    for c,i in dicionario.items():
        if i<=11:
            criança.append(c)
        if i<=17:
            adolescente.append(c)
        if i<=59:
            adulto.append(c)
        else:
            idoso.append(c)
        return novo_dicionario