def agrupa_por_idade(dicionario):
    new_dict = {}
    lista_crianca = []
    lista_adolescente = []
    lista_adulto = []
    lista_idoso = []
    for nome, idade in dicionario.items():
        if idade <= 11:
            lista_crianca.append(nome)
        elif 12 <= idade <= 17:
            lista_adolescente.append(nome)
        elif 18 <= idade <= 59:
            lista_adulto.append(nome)
        else:
            lista_idoso.append(nome)
    new_dict['criança'] = lista_crianca
    new_dict['adolescente'] = lista_adolescente
    new_dict['adulto'] = lista_adulto
    new_dict['idoso'] = lista_idoso
    return new_dict