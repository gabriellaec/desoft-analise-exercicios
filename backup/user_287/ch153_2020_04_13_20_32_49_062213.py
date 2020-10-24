def agrupa_por_idade(d):
    nome = list(d.keys())
    idade = list(d.values())
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    for a in range(len(nome)):
        if idade[a]<=11:
            crianca.append(nome[a])
        elif idade[a]<=17:
            adolescente.append(nome[a])
        elif idades[a]<=59:
            adulto.append(nome[a])
        else:
            idoso.append(nome[a])
    x = {'criança':crianca,'adolescente':adolescente,'adulto':adulto,'idoso':idoso}
    return x