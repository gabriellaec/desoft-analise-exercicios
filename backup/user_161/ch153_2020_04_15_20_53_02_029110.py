def agrupa_por_idade(dicionario_entrada):

    lista_crianca = []
    lista_adolescente = []
    lista_adulto = []
    lista_idoso = []

    for k,v in dicionario_entrada.items():
        if k not in lista_crianca or lista_adolescente or lista_adulto or lista_idoso:
            if v <= 11:
                lista_crianca.append(k)
            elif v > 11 and v <= 17:
                lista_adolescente.append(k)
            elif v > 17 and v <= 59:
                lista_adulto.append(k)
            else:
                lista_idoso.append(k)

    
    dicionario_saida = {"criança": lista_crianca, "adolescente": lista_adolescente, "adulto": lista_adulto, "idoso": lista_idoso}

    return dicionario_saida        