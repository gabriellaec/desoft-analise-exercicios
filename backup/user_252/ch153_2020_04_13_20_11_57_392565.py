def agrupa_por_idade(d):
    dic={}
    a=d.keys()
    for i in a:
        if d[i] [2]<=11:
            return 'criança'
        elif d[i] [2]>=12 or d[i] [2]<=17:
            return 'adolescente'
        elif d[i] [2]>=18 or d[i] [2]<=59:
            return 'adulto'
        else:
            return 'idoso'
        
        
            