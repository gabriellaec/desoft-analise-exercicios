def agrupa_por_idade(d):
    dic={}
    a=d.keys()
    for i in a:
        if d[i] [2]<=11:
            return 'criança'
            dic.append('criança')
            dic.append(d[i])
        elif d[i] [2]>=12 or d[i] [2]<=17:
            return 'adolescente'
            dic.append('adolescente')
            dic.append(d[i])
        elif d[i] [2]>=18 or d[i] [2]<=59:
            return 'adulto'
            dic.append('adulto')
            dic.append(d[i])
        else:
            return 'idoso'
            dic.append('idoso')
            dic.append(d[i])
        
        
        
            