def agrupa_por_idade(dic1):
    dic_faixa={}
    dic_faixa["criança"]=[]
    dic_faixa["adolescente"]=[]
    dic_faixa["adulto"]=[]
    dic_faixa["idoso"]=[]
    for nome in dic1:
        idade=dic1[nome]
        if idade<12:
            idade="criança"
        elif idade>11 and dic1[nome]<18:
            idade="adolescente"
        elif dic1[nome]>17 and dic1[nome]<60:
            idade="adulto"
        else:   
            idade="idoso"
        
        faixa_etaria=idade
        dic_faixa[faixa_etaria].append(nome)
        
    return dic_faixa