def agrupa_por_idade (nome_para_idades):
    idoso = []
    adulto = []
    adolescente = []
    crianca = []
    for nome, idade in nome_para_idades.items():
        if idade <= 11:
            crianca.append(nome_pessoas)
        elif idade <= 17:
            adolescente.append(nome_pessoas)
        elif idade <= 59:
            adulto.append(nome_pessoas)
        else:
            idoso.append(nome)
    faixa_para_nomes = {'crianças' : crianca, 'adolescentes' : adolescente, 'adultos': adulto, 'idoso': idoso}
    return faixa_para_nomes