def agrupa_por_idade(x):
    nomes_das_pessoas=list(x.keys())
    idades_das_pessoas=list(x.values())
    adolescente=[]
    crianca=[]
    adulto=[]
    idoso=[]
    for i in range(len(nomes_das_pessoas)):
        if idades_das_pessoas[i]<=11:
            crianca.append(nomes_das_pessoas[i])
        elif idades_das_pessoas[i]<=17:
            adolescente.append(nomes_das_pessoas[i])
        elif idades_das_pessoas[i]<=59:
            adulto.append(nomes_das_pessoas[i])
        else:
            idoso.append(nomes_das_pessoas[i])
            
    dicionario={"criança":crianca,"adolescente":adolescente,"adulto":adulto,"idoso":idoso}
    return dicionario