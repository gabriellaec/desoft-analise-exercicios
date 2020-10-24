def agrupa_por_idade (dic):

    nomes_crianca = []
    nomes_adolecente = []
    nomes_adulto = []
    nomes_idoso = []

    dic2 = {
        "criança": nomes_crianca,
        "adolescente": nomes_adolecente,
        "adulto": nomes_adulto,
        "idoso": nomes_idoso
    }

    for k,v in dic.items():
        if v <= 11:
            nomes_crianca.append (k)
        elif v>11 and v<18:
            nomes_adolecente.append(k)
        elif v>17 and v<60:
            nomes_adulto.append(k)
        else:
            nomes_idoso.append(k)
    return dic2