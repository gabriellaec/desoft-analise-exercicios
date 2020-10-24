def agrupa_por_idade(dicio={nome: idade}):
    dic={}
    if idade<=11:
        dic.update={criança:[nome]}
        return dic
    if idade>=12 and idade>=17:
        dic.update={adolescente:[nome]}
        return dic
    if idade>=18 and idade<=59:
        dic.update={adulto:[nome]}
        return dic
    else:
        dic.update={idoso:[nome]}
        return dic