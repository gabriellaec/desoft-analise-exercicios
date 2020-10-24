def agrupa_por_idade (nome_para_idade):
    criança = []
    adolescente = []
    adulto = []
    idoso = []
    for nome, idade in nome_para_idade.items():
        if idade <= 11:
            criança.append(nome)
        elif idade <= 17:
            adolescente.append(nome)
        elif idade <= 59:
            adulto.append(nome)
        else:
            idoso.append(nome)
    idade_para_nome = {'criança' : criança, 'adolescente' : adolescente, 'adulto' : adulto, 'idoso' : idoso}
    return idade_para_nome