def agrupa_por_idade(dic1):
    dic_faixa={}
    for nome in dic1:
        if dic1[nome]<12:
            dic1[nome]="criança"
        elif dic1[nome]>11 and dic1[nome]<18:
            dic1[nome]="adolescente"
        elif dic1[nome]>17 and dic1[nome]<60:
            dic1[nome]="adulto"
        else:   
            dic1[nome]="idoso"
        
        if not dic1[nome] in dic_faixa:            
            dic_faixa[dic1[nome]]=[nome]
        
        else:
            dic_faixa[dic1[nome]].append(nome)
        
    return dic_faixa