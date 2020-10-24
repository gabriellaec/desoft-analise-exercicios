def agrupa_por_idade (nome_pessoas):
    idoso = []
    adulto = []
    adolescente = []
    crianca = []
    i = 0
    while i in len(nome_pessoas):
        if nome_pessoas[i] <= 11:
            crianca.append(i)
        elif 12 <= nome_pessoas[i] <= 17:
            adolescente.append(i)
        elif 18 <= nome_pessoas[i] <= 59:
            adulto.append(i)
        else:
            idosos.append(i)
        i += 1