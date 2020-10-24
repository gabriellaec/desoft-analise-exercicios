def agrupa_por_idade(dicionario):
    dicionario2={}
    chaves_crianca=[]
    chaves_adolescente=[]
    chaves_adulto=[]
    chaves_idoso=[]
    for i in dicionario:
         if dicionario[i]<=11:
             chaves_crianca.append(i)
             dicionario2["criança"]=chaves_crianca
         elif 12<=dicionario[i]<=17:
             chaves_adolescente.append(i)
             dicionario2["adolescente"]=chaves_adolescente
         elif 18<=dicionario[i]<=59:
             chaves_adulto.append(i)
             dicionario2["adulto"]=chaves_adulto
         else:
             chaves_idoso.append(i)
             dicionario2["idoso"]=chaves_idoso
    if chaves_crianca==[]:
        dicionario2["criança"]=chaves_crianca
    if chaves_adolescente==[]:
        dicionario2["adolescente"]=chaves_adolescente
    if chaves_adulto==[]:
        dicionario2["adulto"]=chaves_adulto
    if chaves_idoso==[]:
        dicionario2["idoso"]=chaves_idoso
    return dicionario2