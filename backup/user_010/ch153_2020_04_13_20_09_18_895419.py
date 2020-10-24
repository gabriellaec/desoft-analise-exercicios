def agrupa_por_idade (dic):
    crianca=[]
    adolescente=[]
    adulto=[]
    idoso=[]
    for nome,idade in dic.items():
        if idade<=11:
            crianca.append(nome)
        elif idade>11 and idade<=17:
            adolescente.append(nome)
        elif idade>17 and idade<=59:
            adulto.append(nome)
        elif idade>59:
            idoso.append(nome)
    dicionario={"criança":crianca,"adolescente":adolescente,"adulto":adulto,"idoso":idoso}
    return dicionario