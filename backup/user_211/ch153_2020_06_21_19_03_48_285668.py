def agrupa_por_idade(dic):
    novodic={}
    for k,v in dic.items():
        novodic.setdefault('adolescente',[])
        if v <=11:
            novodic.setdefault('criança',[]).append(k)
        elif v>=18 and v<=59:
             novodic.setdefault('adulto',[]).append(k)
        elif v=>60
             novodic.setdefault('idoso',[]).append(k)

    return novodic