def agrupa_por_idade (nomes_idades):
    lista_crianças = []
    lista_adolescentes = []
    lista_adultos = []
    lista_idosos = []
    classificação = {'criança': lista_crianças,'adolescente':lista_adolescentes,'adulto':lista_adultos,'idoso':lista_idosos}
    for i in nomes_idades:
        if nomes_idades[i] <= 11:
            lista_crianças.append(i)
            classificação['criança'] = lista_crianças
        elif nomes_idades[i]<= 17:
            lista_adolescentes.append(i)
            classificação['adolescente'] = lista_adolescentes
        elif nomes_idades[i]<= 59:
            lista_adultos.append(i)
            classificação['adulto'] = lista_adultos
        else:
            lista_idosos.append(i)
            classificação['idoso'] = lista_idosos
    return classificação