def agrupa_por_idade (nome_para_idades):
    idoso = []
    adulto = []
    adolescente = []
    crianca = []
    for nome, idade in nome_para_idades.items():
        if idade <= 11:
            crianca.append(nome)
        elif idade <= 17:
            adolescente.append(nome)
        elif idade <= 59:
            adulto.append(nome)
        else:
            idoso.append(nome)
    faixa_para_nomes = {'crianca' : criança, 'adolescente' : adolescente, 'adulto': adulto, 'idoso': idoso}
    return faixa_para_nomes