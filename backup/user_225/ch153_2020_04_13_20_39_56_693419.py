def agrupa_por_idade (dic):
    listac = []
    listado = []
    listaadu = []
    listaid = []
    novodic = {}
    for elemento in dic:
        if dic[elemento]<=11:
            listac.append(elemento)
        else:
            if 12<=dic[elemento]<=17:
                listado.append(elemento)
            elif 18<=dic[elemento]<=59:
                listaadu.append(elemento)
            else:
                listaid.append(elemento)
    novodic['criança']=listac
    novodic['adolescente']=listado
    novodic['adulto']=listaadu
    novodic['idoso'] = listaid
    return novodic