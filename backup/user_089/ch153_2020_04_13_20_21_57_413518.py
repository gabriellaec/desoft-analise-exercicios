def agrupa_por_idade(dic):
    novo = {}
    listac = []
    lista = [[]]
    listaA = []
    listai = []
    for e,v in dic.items():
        if v <= 11:
            listac.append(e)
            novo["criança"] = listac
        if 12 <= v <= 17:
            lista.append(e)
            novo["adolescente"] = lista
        if 18 <= v <= 59:
            listaA.append(e)
            novo["adulto"] = listaA
        if v >= 60:
            listai.append(e)
            novo["idoso"] = listai
    return novo
        