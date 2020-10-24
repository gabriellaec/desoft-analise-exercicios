def agrupa_por_idade(dicio):
    novo_dicio={}
    kid=[]
    teen=[]
    adult=[]
    senior=[]
    for i in dicio:
        if dicio[i]<=11:
            kid.append(i)
            novo_dicio["criança"]=kid
        elif 12<=dicio[i]<=17:
            teen.append(i)
            novo_dicio["adolescente"]=teen
        elif 18<=dicio[i]<=59:
            adult.append(i)
            novo_dicio["adulto"]=adult
        else:
            senior.append(i)
            novo_dicio["idoso"]=senior
    if kid==[]:
        novo_dicio["criança"]=kid
    if teen==[]:
        novo_dicio["adolescente"]=teen
    if adult==[]:
        novo_dicio["adulto"]=adult
    if senior==[]:
        novo_dicio["idoso"]=senior
    return novo_dicio