def agrupa_por_idade(dic1):
    dic1={}
    nome=dic1.keys()
    idade=dic1.values()
    dic1['nome']=idade
    for nome in dic1:
        dic2={}
        if dic1[nome]<=11:
            dic2['criança']=nome
        elif dic1[nome]>11 and dic1[nome]<=17:
            dic2['adolescente']=nome
        elif dic1[nome]>17 and dic1[nome]<=59:
            dic2['adulto']=nome
        return dic2
            
            