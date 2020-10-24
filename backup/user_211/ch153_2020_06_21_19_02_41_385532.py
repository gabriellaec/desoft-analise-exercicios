def agrupa_por_idade(dic):
    novodic={}
    for k,v in dic.items():
        novodic.setdefault('adolescente',[])
        if v <=11:
            novodic.setdefault('crianca',[]).append(k)
        elif v>=18 and v<=59:
             novodic.setdefault('adulto',[]).append(k)
        else:
             novodic.setdefault('idoso',[]).append(k)

    return novodic