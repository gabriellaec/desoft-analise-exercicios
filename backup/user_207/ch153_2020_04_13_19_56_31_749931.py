def agrupa_por_idade (pessoas):
    crianca =[]
    adolescente =[]
    adulto =[]
    idoso =[]
    novo_dic ={}
    for pessoa, idade in pessoas.items():
        if idade <= 11:
            crianca.append (pessoa)
        elif idade >= 12 and idade <= 17:
            adolescente.append (pessoa)
        elif idade >= 18 and idade<= 59:
            adulto.append (pessoa)
        else:
            idoso.append (pessoa)
    novo_dic['crianca'] = crianca
    novo_dic['adolescente'] = adolescente
    novo_dic['adulto']= adulto
    novo_dic['idoso'] = idoso
    return novo_dic