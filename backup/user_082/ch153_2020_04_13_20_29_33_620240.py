def agrupa_por_idade(nome):
    faixas_etarias = {
        crianca : [],
        adolescente : [],
        adulto : [],
        idoso: [],
    }
    for i in range(nome):
        idade= nome.get[i]
        if idade <= 11:
            crianca.append(nome)
        if idade >= 12 and idade <= 17:
            adolescente.append(nome)
        if idade >= 18 and idade <= 59:
            adulto.append(nome)
        if idade >= 60:
            idoso.append(nome)
