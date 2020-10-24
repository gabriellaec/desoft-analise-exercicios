def agrupa_por_idade(dicionome):
    diciogrupo={}
    crianca=[]
    adolescente=[]
    adulto=[]
    idoso=[]
    
    for i,j in dicionome.items():
        if j<=11:
            crianca.append(i)
        elif j<=17:
            adolescente.append(i)
        elif j<=59:
            adulto.append(i)
        else:
            idoso.append(i)

    diciogrupo["criança"]=crianca
    diciogrupo["adolescente"]=adolescente
    diciogrupo["adulto"]=adulto
    diciogrupo["idoso"]=idoso
    return diciogrupo
    