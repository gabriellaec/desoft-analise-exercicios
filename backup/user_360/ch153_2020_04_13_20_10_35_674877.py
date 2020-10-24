def agrupa_por_idade (dicionario):
    #cri -> criança
    #adl -> adolescente
    #adt -> adulto
    #ids -> idoso
    cri = []
    adl = []
    adt = []
    ids = []
    dicionario1 = {"criança": cri, "adolescente": adl, "adulto": adt, "idoso": ids }
    for i,c in dicionario.items():
        if c <= 11:
            cri.append (i)
        elif c>11 and c<18:
            adl.append(i)
        elif c>17 and c<60:
            adt.append(i)
        else:
            ids.append(i)
    return dicionario1
    