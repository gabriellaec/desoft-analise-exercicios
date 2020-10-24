
def agrupa_por_idade(dic):
    nomes=list(dic.keys())
    idades=list(dic.values())
    crianca=[]
    adolescente=[]
    adulto=[]
    idoso=[]
    for i in range(len(nomes)):
        if idades[i]<