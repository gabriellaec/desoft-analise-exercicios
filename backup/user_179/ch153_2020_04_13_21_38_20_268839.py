def agrupa_por_idade (dicionario):
    # Criei listas para separar quais pessoas estão em qual faixa etária
    crianca = []
    adolescente = []
    adulto = []
    idoso = []
    faixa_etaria = {}
    # Separei as keys e os valores do dicionário para ficar mais fácil adicionar os valores
    # que eu quero depois nas listas. Como eles tem o index deles em comum, achei que seria melhor.
    nome = list(dicionario.keys())
    idade = list(dicionario.values())
    i = 0
    # Fui adicionando em cada lista os respectivos nomes que tem sua idade de acordo.
    while i < len(dicionario):
        if idade[i] <= 11:
            crianca.append(nome[i])
            i = i + 1
        elif idade[i] > 12 and idade[i] <= 17:
            adolescente.append(nome[i])
            i = i + 1
        elif idade[i] > 18 and idade[i] <= 59:
            adulto.append(nome[i])
            i = i + 1
        else:
            idoso.append(nome[i])
            i = i + 1
    # Por fim, só montei o dicionário com as respectivas faixas etárias junto ao nome das pessoas 
    # que tem essa idade.
    faixa_etaria['criança'] = crianca
    faixa_etaria['adolescente'] = adolescente
    faixa_etaria['adulto'] = adulto
    faixa_etaria['idoso'] = idoso
    return faixa_etaria