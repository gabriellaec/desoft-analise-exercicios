def agrupa_por_idade(dicionario):
    dic = {"criança": , "adolescente": , "adulto": , "idoso": }
    for nome,idade in dicionario.items():
        if idade <= 11:
            dic["criança"] += [nome]
        elif idade > 11 and idade <=17:
            dic["adolescente"] +=[nome]
        elif idade >17 and idade <=59:
            dic["adulto"] += [nome]
        else:
            dic["idoso"] += [nome]
    return dic
        