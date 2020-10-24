def agrupa_por_idade(dicionario):
    novo_dic = {'criança':[],'adolescente':[], 'adulto':[],'idoso':[]}
    for i in dicionario:
        idade = dicionario[i]
        if idade <= 11:
            criança = []
            if novo_dic['criança']==[]:
                criança.append(i)
                novo_dic['criança']= criança
            else:
                criança.append(i)
                novo_dic['criança']+=criança
        if idade > 11 and idade < 18:
            adolescente =[]
            if novo_dic['adolescente']==[]:
                adolescente.append(i)
                novo_dic['adolescente']=adolescente
            else:
                adolescente.append(i)
                novo_dic['adolescente']+=adolescente
        if idade >= 18 and idade < 60:
            adulto = []
            if novo_dic['adulto']==[]:
                adulto.append(i)
                novo_dic['adulto']= adulto
            else:
                adulto.append(i)
                novo_dic['adulto']+=adulto
        if idade >= 60:
            idoso = []
            if novo_dic['idoso']==[]:
                idoso.append(i)
                novo_dic['idoso']= idoso
            else:
                idoso.append(i)
                novo_dic['idoso']+=idoso
    return novo_dic