def agrupa_por_idade (dicionario):
    criança = []
    adolescente = []
    adulto = []
    idoso = []
    dicionario1 = {"criança": criança, "adolescente": adolescente, "adulto": adulto, "idoso": idoso }
    for i,c in dicionario.items():
        if c <= 11:
            criança.append (i)
        elif c>11 and c<18:
            adolescente.append(i)
        elif c>17 and c<60:
            adulto.append(i)
        else:
            idoso.append(i)
    return dicionario1
    
        